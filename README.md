Student CRM allows a user to view & save information of student in a department/class.

![Student_CRM Home](/static/studentcrm_home.png) 

Table of Contents
----------
- [Technologies Used](https://github.com/AdityaRajuladevi/StudentCRM_APP#technologies-used)
- [Installation](https://github.com/AdityaRajuladevi/StudentCRM_APP#installation)
- [Admin Account Setup](https://github.com/AdityaRajuladevi/StudentCRM_APP#admin-account-setup)
- [Server Setup](https://github.com/AdityaRajuladevi/StudentCRM_APP#server-setup)
- [Basic Usage](https://github.com/AdityaRajuladevi/StudentCRM_APP#basic-usage)
- [Choices I Made](https://github.com/AdityaRajuladevi/StudentCRM_APP#choices-i-made)
- [About the Author](https://github.com/AdityaRajuladevi/StudentCRM_APP#about-the-author)


Technologies used
----------
- Python backend
- Django web framework
- HTML/CSS
- Bootstrap

Installation
-----------
Clone this repo to your machine. If you need help with this part, GitHub has [great documentation](https://help.github.com/articles/fork-a-repo/) -- follow along up to, but not including, Step 3.

We need to create a virtual environment in our copy of the repository, so that the technologies you download to make Student CRM work don't interfere with any other technologies you may have installed on your computer. To do this, make sure you're in the ` StudentCRM_APP/ ` directory then type the following in your Terminal:

` $ virtualenv env `

Next, type ` $ source env/bin/activate ` to create a "bubble" around the workspace.

You will see that there is now '(env)' in front of the command line prompt: ` (env) $ `

It is worth mentioning the .gitignore file at this point. There are certain files that we don't want or need to commit to the repository, and the names of those files will go inside a different file called ` .gitignore `. When we eventually do make our commits, git will automatically ignore the files listed inside the .gitignore file. The .gitignore file is already included in the StudentCRM_APP repository you cloned -- you don't need to do anything here.

We now need to install all the libraries and technologies that appear in the file ` requirements.txt `. From the ` StudentCRM_APP/ ` directory (which you should still be in), simply type the following into your Terminal:

` (env) $ pip install -r requirements.txt `

You should see a success message similar to this at the bottom of the Terminal window:

``` python
Installing collected packages: pytz, Django, six, shortuuid, django-shortuuidfield, reverse
Successfully installed Django-2.0.4 django-shortuuidfield-0.1.3 pytz-2018.4 reverse-0.1.0 shortuuid-0.5.0 six-1.11.0pud
```

Admin Account Setup
-----------
We're getting so close! Let's create an admin. Run this command in the Terminal and follow the prompts to enter your name, email and password:

` python manage.py createsuperuser `


Server Setup
-----------
Woo hoo! You're now ready to run your server! Using the same Terminal tab from the steps we just completed for the admin, type the following command in your Terminal:

` (env) $ python manage.py runserver `
If all went well, you'll receive a success message similar to this:

```
python manage.py runserver
Performing system checks...

System check identified no issues (0 silenced).
April 23, 2018 - 00:31:59
Django version 2.0.4, using settings 'studentcrm.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
[23/Apr/2018 00:32:17] "GET / HTTP/1.1" 200 4700
```

You can now visit the URL ` http://localhost:8000 ` in your web browser and you should see the navbar on the home page! There won't be any campaigns listed on the home page, because you haven't created any yet.

![Student CRM Homepage](/static/studentcrm_home.png)


Basic Usage
-----------
### 1. Go to Home
* Visit ` http://localhost:8000/ ` or ` http://localhost:8000/home ` that will take you to the home page of the application .

### 2. Signup your course/department
* The home page provides a link that will allow you to register to the CRM ` http://localhost:8000/signup/ `
* You should provide all the required details to register the user

### 3. Viewing your Students List
* Clicking on a students tab on the home page will take you to that student's list page: ` http://localhost:8000/list/ `,  Remember to use the pagination feature at the bottom of each page to access all of the students!


Choices I Made
-----------

- I created a sample application to test my understanding of the Django framework that I have learned recently. 

- I used Django because I wanted to learn a new Python web framework. The documentation is AWESOME!


About the author
-----------
[LinkedIn - Aditya Rajuladevi](https://www.linkedin.com/in/aditya-rajuladevi-56244868/ "Aditya Rajuladevi's LinkedIn profile")

I'm a Master's student at University of Nevada, Las Vegas. I am from a computer science background with interests in software development including web and mobile, and a machine learning enthusiast. 
