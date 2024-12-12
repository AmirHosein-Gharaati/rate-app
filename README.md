# Rating app

## Project setup

- Setup virtual environment

```bash
virtualenv venv
source venv/bin/activate
```

- Install dependencies
```bash
pip install -r requirements.txt
```

- Create database
```bash
python manage.py makemigrations
python manage.py migrate
```

- Spin off docker compose
```bash
docker compose up -d
```

- Run the project
```bash
python manage.py runserver
```

- Start Celery/Beat
```bash
celery -A tasks worker -l info
celery -A tasks beat -l info
```