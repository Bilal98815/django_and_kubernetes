import time
import csv
# import os
import gzip
import datetime

from django.core.management.base import BaseCommand
from django.db import connection

from io import TextIOWrapper


class Command(BaseCommand):
    help = "Query the database"

    def get_queries(self):
        """Get all queries from the database"""
        # with connection.cursor() as cursor:
        #     cursor.execute("""SELECT usename, pid, datname, application_name, query_start,
        #                    wait_event_type, wait_event, state, query FROM pg_stat_activity
        #                    ORDER BY query_start""")
        #     result = cursor.fetchall()
        with connection.cursor() as cursor:
            cursor.execute("""SELECT name, description, slug, created_at,
                           last_modified FROM practice_app_practicemodel""")
            result = cursor.fetchall()
        return result

    def save_to_csv(self, queries):
        """Saving the queries to a csv file"""

        # current_date = datetime.datetime.now().strftime('%Y-%m-%d')
        current_datetime = datetime.datetime.now().strftime('%Y-%m-%d_%H:%M:%S')
        file_path = f'{current_datetime}.csv.gz'
        # gs_file_path = f'db001/{current_date}/{file_path}'

        with gzip.open(file_path, 'wb') as f:
            with TextIOWrapper(f, encoding='utf-8', newline='') as csvfile:
                writer = csv.writer(csvfile)
                # writer.writerow(['usename', 'pid', 'datname', 'application_name', 'query_start',
                #                 'wait_event_type', 'wait_event', 'state', 'query'])
                writer.writerow(['name', 'description', 'slug', 'created_at', 'last_modified'])
                for query in queries:
                    writer.writerow(query)
        # os.remove(file_path)

    def handle(self, *args, **kwargs):
        while True:
            queries = self.get_queries()
            if queries:
                self.save_to_csv(queries)
            time.sleep(300)   # sleep for 5 minutes before querying again
