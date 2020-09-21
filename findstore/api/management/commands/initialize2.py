from pathlib import Path
import pandas as pd
from django.core.management.base import BaseCommand
from findstore import settings
from api import models


class Command(BaseCommand):
    help = "initialize database"
    DATA_DIR = Path(settings.BASE_DIR).parent / "data"
    DATA_FILE = str(DATA_DIR / "total_review_df.pkl")

    def _load_dataframes(self):
        try:
            data = pd.read_pickle(Command.DATA_FILE)
        except:
            print(f"[-] Reading {Command.DATA_FILE} failed")
            exit(1)
        return data

    def _initialize(self):
        """
        Sub PJT 1에서 만든 Dataframe을 이용하여 DB를 초기화합니다.
        """
        print("[*] Loading data...")
        dataframes = self._load_dataframes()

        print("[*] Initializing stores...")
        models.Reviews.objects.all().delete()
        
        reviews_bulk = [
            models.Reviews(
                res_id=reviews.res_id,
                res_name=reviews.res_name,
                user_name=reviews.user_name,
                rating=reviews.rating,
                review=reviews.review,
                sex=reviews.sex,
                age=reviews.age,
                ppl=reviews.ppl
            )
            for reviews in dataframes.itertuples()
        ]
        models.Reviews.objects.bulk_create(reviews_bulk)

        print("[+] Done")

    def handle(self, *args, **kwargs):
        self._initialize()