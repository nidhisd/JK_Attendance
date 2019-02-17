# Jk Attendance:

## Introduction: 
  The application is developed to encourage community involvement of kids by rewarding them depending on the number of attendances marked. 
  It is developed in Python using Django Framework. Once logged in by a supervisor, Kids will be able to mark their attendance using a       personal identification number.
  
  Key highlights:
  1. Supervisor Login/Logout.
  2. Ability to add participants by supervisor.
  3. Leaderboard.
  4. Ability to mark attendance only during community hours.
  5. Erroring out when invalid user, or marking attendance during invalid hours and also if already marked.

## Running Locally:

1. Clone the git repo:
```
git clone git@github.com:nidhisd/JK_Attendance.git
```
Ensure that necessary environment variables are configured in .env file of the git repo.

2. Migrate models:
```
python manage.py makemigrations
python manage.py migrate
```
3. Create Superuser:
```
python manage.py createsuperuser
```
4. Run the App:
```
python manage.py runserver
```
5. Add Supervisor credentials on admin:
    Enter the supervisor details on admin console of the app.
 
    http://localhost:8000/admin

6. Run locally:
  
    http://localhost:8000


## Deploying on Production(Heroku):

1. Login to Heroku:
```
heroku login
```
2. Cloning the repo from git:
```
git clone git@github.com:nidhisd/JK_Attendance.git
```

3. Create Staging on Heroku:
Ensure that necessary environment variables are configured on Heroku in the .env file of the git repo.
```
heroku create -a jk-attendance
```
4. Deploy on Heroku:
```
git push heroku master
```
Ensure that at least one instance of the app is running;
```
heroku ps:scale web=1
```
5. Migrate the Django models:

After successfully deploying app on heroku, make sure to have all the necessary migrations done;

```
heroku run bash
python manage.py migrate
```
6. Add the superuser to the heroku DB:
```
heroku run bash
python manage.py createsuperuser
```
7. Add supervisor credentials on admin console:

    https://jk-attendance.herokuapp.com/admin

8. Run the App on web:
  
    *Voila!* The app can be run on any browser:
  
    https://jk-attendance.herokuapp.com


The [SO](https://stackoverflow.com/questions/32600341/how-to-deploy-migrate-an-existing-django-app-project-to-a-production-server/32601033#32601033) page has very simplified steps to deploying on Heroku.

## Screenshots:


## Home:
![Home](https://github.com/nidhisd/JK_Attendance/blob/master/jk_attendance/Screenshots/home.png)


## Login:
![Login](https://github.com/nidhisd/JK_Attendance/blob/master/jk_attendance/Screenshots/login.png)


## Success:
![Success](https://github.com/nidhisd/JK_Attendance/blob/master/jk_attendance/Screenshots/success.png)


## Leaderboard:
![Leaderboard](https://github.com/nidhisd/JK_Attendance/blob/master/jk_attendance/Screenshots/leaderboard.png)


## Error if already marked:
![Error if already marked](https://github.com/nidhisd/JK_Attendance/blob/master/jk_attendance/Screenshots/already_marked.png)

## Future Implementations:

- [ ] Adding favicon.
- [ ] Adding Logo to navbar.
- [ ] Analytics of overall and agewise attendance.
- [ ] Analytics of individual user.
- [ ] Ability to scan barcode to automatically feed id.



