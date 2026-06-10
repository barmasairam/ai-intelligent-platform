from sqlalchemy import create_engine, text
import random
from datetime import datetime, timedelta

engine = create_engine("sqlite:///db/database.db")

with engine.begin() as conn:
    conn.execute(text("DROP TABLE IF EXISTS sales"))

    conn.execute(text("""
    CREATE TABLE sales(
        date TEXT,
        product TEXT,
        sales INTEGER
    )
    """))

    # generate 60 days data
    start_date = datetime(2024, 1, 1)

    for i in range(60):
        date = start_date + timedelta(days=i)

        laptop_sales = 1000 + i*5 + random.randint(-100, 100)
        phone_sales = 600 + i*3 + random.randint(-80, 80)

        conn.execute(text("""
        INSERT INTO sales VALUES (:date, :product, :sales)
        """), [
            {"date": str(date.date()), "product": "Laptop", "sales": laptop_sales},
            {"date": str(date.date()), "product": "Phone", "sales": phone_sales}
        ])

print("✅ Large dataset created")