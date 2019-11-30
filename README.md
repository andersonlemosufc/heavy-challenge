# Heavy Challenge

This project consists of developing a Django backend that works as a web service (using API Rest) and a frontend that uses Angular and gets data from the web service.
After downloading the project, you can run both backend and frontend using the steps described below.
Run the following commands on the Linux terminal (you can easily find how to perform the procedures below similarly on Windows or macOS).

### How to run Django backend

The application was written using Python 2.7.15 and pip 19.3.1. You can install these versions or similar versions.

- ##### To install Python, run the commands:

	`$ sudo apt-get update`
	
	`$ sudo apt-get install build-essential checkinstall`
	
	`$ sudo apt-get install libreadline-gplv2-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev`
	
	`$ cd /usr/src`
	
	`$ sudo wget https://www.python.org/ftp/python/2.7.16/Python-2.7.16.tgz`
	
	`$ sudo tar xzf Python-2.7.16.tgz`
	
	`$ cd Python-2.7.16`
	
	`$ sudo ./configure --enable-optimizations`
	
	`$ sudo make altinstall`

- ##### To install pip, run the commands:

	`$ curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py`
	
	`$ sudo python get-pip.py`

It is common to make and use a different virtual environment for each Django project. To create Python virtual environments, we can use the virtualenv program.

- ##### To install virtualenv, simply run the command below:

	`$ pip install virtualenv`

- ##### Create a virtual environment to run the project:

	`$ mkvirtualenv my_project`

	- Once created, to use the same virtual environment (in another terminal, or when we close the terminal we are using, for example), simply execute the command:
	
	`$ workon my_project`

Since you already downloaded the project, navigate to the project root folder and enter the "back_django" folder (which is where the backend is). Then install the required dependencies described in the "requirements.txt" file. These dependencies include Django itself, Django Rest Framework, and the django-cors-headers library, which allows us to test the server and client on the same machine without the same-origin policy problem. It requires at least Django version 1.11 (without it we could use Django version 1.9).

- ##### To install all these dependencies, simply run the command:

	`$ pip install -r requirements.txt`

- ##### To create the database, we run:

	`$ python manage.py makemigrations`
	
	`$ python manage.py migrate`

- ##### We can insert predefined data into the database (for testing). To do this, run:

	`$ python manage.py loaddata users.json`
	
	`$ python manage.py loaddata reports.json`
	
	`$ python manage.py loaddata responses.json`

- ##### Finally, to run the server, simply run the command:

	`$ python manage.py runserver`

The server runs at http://127.0.0.1:8000 and contains two endpoints, reports and users, to fetch reports and users saved in the database. At the reports endpoint, we can optionally give the following GET parameters:
- user_id (int): If given, returns only reports related to users with that id (reports in which he is the author, supervisor, or gave a response).
- pagination_offset (int): An offset to the response list (i.e., from which position reports should be retrieved).
- pagination_limit (int): The maximum number of reports to retrieve.

### How to run Angular front-end

Just enter the project root folder, enter the "front_angular" folder and then open the "index.html" file in some browser.

### Questions

You can contact me at the following email address: andersonlemos.ufc@gmail.com.

