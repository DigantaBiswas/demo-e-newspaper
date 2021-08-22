# Demo News app

To get the project go to github [link](https://github.com/DigantaBiswas/demo-e-newspaper) . The master branch is updated . so just clone the repo and follow next steps for installation. 

## Installation
After cloning the project from github create a virtual env ,and active the virtual env . Now intstall the requirements to the env you just created. 

```bash
pip install -r requirements.txt
```

Now you need to migrate the tables. To migrate execute following command in the terminal 


```bash
python manage.py makemigrations

python manage.py migrate
```


Now you go to the project dir where the manage.py file resides. You need to create a super user by executing this command -

```bash
python manage.py createsuperuser
```
Now you can use the application just run the surver by using -


```bash
python manage.py runserver 
```

To run the celery worker that fetch data from the API you need to run this command -

```bash
celery -A demo_e_newspaper worker --beat -l info -S django
```

## Features

- User Ragistration , Authentication
- User Authentication Token for mobile users
- User Based news filter feature  
- Landing page shows the top newses in database
- Scheduler based api data fetch 
- Management command to test the scheduler function manually(newspaper>management>command folder)
- Other api support to  expose feature for postman, mobile or ther platforms 

## Important Api list 
```bash
    'accounts/api/user/' #user list
    'accounts/api/user/<pk>/' #user details
    'accounts/api/user-settings/' #user filtering config list
    'accounts/api/user-settings/<pk>/'# user's filter details edit 
    'accounts/api/token-auth/' #token based authentication
    'accounts/api/logout/' #distroy api token

    'newspaper/api/personalized-news/' #get personalized news api 
```

## Note
- My apologies that I could not implement the sendgrid email feature as the sendgrid
 website was not giving me permissions to create api key . And as for today the site was down . But I think as I used 
celery for async task , the mail task was similar to that . 

- And the news api does not return the country as response , so a possible solutions
was to  manually make a list of country keyword and use that to filter the news and store it in the data base
to trac the country. But as I was already late so I just covered the main topics that covers important libraries . 