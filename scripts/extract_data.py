import os
import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine


load_dotenv()

host = os.getenv("DB_HOST")
dbname = os.getenv("DB_NAME")
user = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")

db_url = f"postgresql+psycopg2://{user}:{password}@{host}/{dbname}"

engine = create_engine(db_url)


query = """
SELECT
    c.customer_id,
    c.age,
    c.club_member_status,
    a.article_id,
    a.prod_name,
    a.product_group_name,
    a.product_type_name,
    a.colour_group_name,
    t.price,
    t.t_dat,
    t.sales_channel_id

FROM transaction_2019 t

JOIN articles a
    USING (article_id)

JOIN customers c
    USING (customer_id)
"""


data_2019 = pd.read_sql_query(query, con=engine)

data_2019.to_csv(
    "data/processed/hm_2019.csv",
    index=False
)