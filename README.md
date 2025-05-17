# Fiko-Backend

[![](https://img.shields.io/badge/Python-3.12.4-orange)](https://www.python.org/)
[![](https://img.shields.io/badge/Django-5.2.1-green)](https://www.djangoproject.com/)


## Resolve customer requests instantly with AI customer service






## How to run

1. Clone this repository

```bash
git clone https://github.com/nimadorostkar/Fiko-Backend.git
```

2. Install dependencies

```bash
pip install -r requirements/development.txt 
```

3. Make .env file (use either prod.env.template or dev.env.template to create .env file)

4. Run the following commands to get started (Development)

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

5. Make sure you have Postgredb running (Production)

6. you can run them manually, after the containers spin up, like so:

```bash
docker-compose exec web python manage.py makemigrations
docker-compose exec web python manage.py migrate   
docker exec -it container_id python manage.py createsuperuser

```


7. Build the image and spin up the two containers

```bash
docker-compose up -d --build
```



 enjoy!