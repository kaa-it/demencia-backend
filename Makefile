run:
	python manage.py runserver
migrate:
	python manage.py makemigrations
	python manage.py migrate
lint:
	isort ./ && flake8 ./
packages:
	pip install -r ./requirements/dev.txt
superuser:
	python manage.py createsuperuser
files:
	python manage.py collectstatic --no-input
fixtures:
	python manage.py load_geocodes
	python manage.py loaddata demencia/fixtures/data.json