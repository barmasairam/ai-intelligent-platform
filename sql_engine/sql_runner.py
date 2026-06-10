from sqlalchemy import create_engine, text

engine = create_engine("sqlite:///db/database.db")

def run_sql_query(query):

    q = query.lower()

    if "laptop" in q:
        sql = "SELECT * FROM sales WHERE product='Laptop'"
    elif "phone" in q:
        sql = "SELECT * FROM sales WHERE product='Phone'"
    elif "total" in q:
        sql = "SELECT SUM(sales) as total FROM sales"
    else:
        sql = "SELECT * FROM sales"

    with engine.connect() as conn:
        result = conn.execute(text(sql))
        return [dict(row._mapping) for row in result]