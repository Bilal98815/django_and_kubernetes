while ! nc -z postgres-service 5432; do
  echo "Waiting for the PostgreSQL database to be ready..."
  sleep 1
done

echo "Database is ready. Running migrations and starting the server."

poetry run python manage.py query_database