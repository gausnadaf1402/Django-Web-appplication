Set Up Instruction:-
1) first we have to activate virtual environment in our local machine.
2) create our dango project inside our created virtual environment.
3) installed packages.
4) create django project.
5) inside project created one app named myapp.

Breif Explanation of project:
first of all added app name inside the settings file because it is important to run our application.
then i have created forms.py file inside the app then add field of that form where we upload the csv file. written the logic in views.py file for file uploading.
performs data analysis using pandas and numpy, and displays the results and
visualizations on the web interface.
include urls in project file i.e path('analysis',include('myapp.urls')).  and created actual url inside our url file of app. which path display on browser
run the project using this commond  python manage.py runserver.
