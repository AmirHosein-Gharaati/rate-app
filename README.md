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

## Simulation

### Database
In order to create 1000 posts using SQL in docker, you can run the
following command in terminal:
```bash
docker exec -i rating_app-db-1 psql -U postgres -d rate_app <<EOF
INSERT INTO posts_post (title, rate_average, user_count)
SELECT 
    CONCAT('Post ', num) AS title,
    0.0 AS rate_average,
    0 AS user_count
FROM 
    GENERATE_SERIES(1, 1000) AS num;
EOF
```

### Users
Using `Grafana K6` tool, we can simulate the user requests. The script is located in the `simulcation/k6` directory.
More information about the scenario is mentioned in the k6 [README](./simulation/k6/README.md) file.
