from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Sum
from django.http import HttpResponse
from django.db import IntegrityError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.utils import timezone
import datetime
from .models import Participant, Attendance

# Create your views here.
def home(request):
    return render(request, 'home.html')

def leaderboard(request):
    '''
         This method will show the leaderboard of all competing participants
    '''
    participant_list = Participant.objects.all().order_by('-points')
    for first_name, points in enumerate(participant_list):
        if points is None:
            participant_list.update(points = 0)
        print(points)
    return render(request, 'leaderboard.html', {'participant_list' : participant_list})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form })

def login(request):
   return render(request, 'login.html')

def get_am_pm(cd):
    '''
         This method will help determine if the time_of_day is AM or PM
    '''

    current_time = cd.time()
    print(current_time)
    morning_start = datetime.time(3, 0, 0)
    morning_end = datetime.time(12, 0, 0)
    evening_start = datetime.time(12, 0, 0)
    evening_end = datetime.time(23, 59, 59)
    if morning_start <= current_time <= morning_end :
        return 'AM'
    elif evening_start <= current_time <= evening_end :
        return 'PM'
    else:
        return None

def update_points(participant_id, total_points):
    ''' 
        This method will update points in the Participant object after sucessfully 
        marking attendance 
    '''

    participant = Participant.objects.get(id=participant_id)
    if total_points is None:
        total_points = 0
    participant.points = total_points
    participant.save()

def get_points(participant, am_pm, request):
    ''' 
        This method will decide points depending on time_of_day 
    '''
    if am_pm is None:
        return render(request, 'not_eligible_to_mark.html', {'firstname': participant.first_name})
    else:
        if am_pm == 'AM':
            points = 10
        elif am_pm == 'PM':
            points = 5
        else:
            points = 0
        return points
            

@login_required(login_url='/accounts/login/')
def mark_attendance(request):
    '''
         This method will mark attendance by making an entry in the Attendance
         table.
    '''
    if request.POST.get('barcode'):
        try:
            barcode = request.POST.get('barcode')
            participant = get_object_or_404(Participant, barcode=request.POST.get('barcode'))
        except Exception as e:
            print(e)
            return render(request, 'error_miscellaneous.html')
        else:
            current_date_time = timezone.localtime(timezone.now())
            am_pm = get_am_pm(current_date_time)
            points = get_points(participant, am_pm, request)
            print(points)
            try:
                attendance = Attendance.objects.create(participant = participant,
                                                       datetime_attendance_logged = current_date_time,  
                                                       time_of_day =am_pm, 
                                                       points=points)
                attendance.save()
            except IntegrityError as e:
                print(e)
                return render(request, 'already_marked.html', {'firstname': participant.first_name})
            else:
                participant_id = participant.id
                total_points = Attendance.objects.filter(participant_id=participant.id).aggregate(Sum('points'))
                total = Attendance.objects.values('participant_id').annotate(total=Sum('points')).order_by('-total')
                #print(total)
                points = total_points['points__sum']
                print(points)
                update_points(participant.id, points)
                print(points)
                return render(request, 'success.html', {'points': points, 'first_name': participant.first_name })

    
    return render(request, 'mark_attendance.html')

