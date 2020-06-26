1) Run this command to install dependencies:
	pip install -r requirements.txt

2) Run this command to populate database with dummy data using fake values:
	python manage.py load_dummy_data <count>

   number of users to populate can be given in the arguement "count". It is optional, by default it generates data for 20 users.

3) The url of the API to get the data is
	/api/getdata/