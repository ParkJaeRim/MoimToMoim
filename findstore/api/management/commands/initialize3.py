from pathlib import Path
import pandas as pd
from django.core.management.base import BaseCommand
from findstore import settings
from api import models


class Command(BaseCommand):
    help = "initialize database"
    DATA_DIR = Path(settings.BASE_DIR).parent / "data"
    DATA_FILE = str(DATA_DIR / "ent_df.pkl")

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
        models.EnterStore.objects.all().delete()
        
        # stores = dataframes["stores"]
        enterstores_bulk = [
            models.EnterStore(
                name=enterstore.name,
                address=enterstore.address,
                tel=enterstore.tel,
                category=enterstore.category,
                main_mn=enterstore.main_mn,
                price=enterstore.price,
                menu=enterstore.menu,
                opng_tm=enterstore.opng_tm,
                rating=enterstore.rating,
                rvw_cnt=enterstore.rvw_cnt,
                tags=enterstore.tags,
                img=enterstore.img
            )
            for enterstore in dataframes.itertuples()
        ]
        models.EnterStore.objects.bulk_create(enterstores_bulk)

        print("[+] Done")

    def handle(self, *args, **kwargs):
        self._initialize()