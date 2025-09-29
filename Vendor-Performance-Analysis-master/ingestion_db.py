from sqlalchemy import create_engine

import pandas as pd

import os
import logging
import time

logging.basicConfig(
    filename="logs/ingestion_db.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filemode="a",
)

engine = create_engine("sqlite:///inventory.db")


def ingest_db(df, table_name, engine, if_exists="replace"):
    df.to_sql(table_name, con=engine, if_exists=if_exists, index="False")


def load_raw_data():
    """Loads CSVs as dataframe and ingests into db"""
    start = time.time()

    for file in os.listdir("data"):
        if file.endswith(".csv"):
            file_path = os.path.join("data", file)
            table_name = file[:-4]
            logging.info(f"Ingesting {file} into db")

            chunksize = 50000
            first_chunk = True  # replace only once

            for chunk in pd.read_csv(file_path, chunksize=chunksize):
                if first_chunk:
                    ingest_db(chunk, table_name, engine, if_exists="replace")
                    first_chunk = False
                else:
                    ingest_db(chunk, table_name, engine, if_exists="append")

    end = time.time()
    total_time = (end - start) / 60
    logging.info("----------Ingestion Complete----------")
    logging.info(f"Total time taken: {total_time:.3f} minutes")


if __name__ == "__main__":
    load_raw_data()
