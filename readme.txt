A Django web application which generates fake data using Faker and saves in the database. We can use Custom management command to populate any no. of data in database.

1) Run this command to install dependencies:
	pip install -r requirements.txt

2) Run this command to make migrations:
	python manage.py makemigrations

3) Run this command to migrate:
	python manage.py migrate

2) Run this command to populate database with dummy data using fake values:
	python manage.py load_dummy_data <count>

   number of users to populate can be given in the arguement "count". It is optional, by default it generates data for 20 users.

3) The url of the API to get the data is
	/api/getdata/
