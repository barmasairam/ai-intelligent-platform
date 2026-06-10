from router import route_query
from sql_engine.sql_runner import run_sql_query
from ml_engine.model import predict_sales
from insight_engine.insight import generate_insight

def handle_query(query):

    route = route_query(query)

    if route == "sql":
        data = run_sql_query(query)
        insight = generate_insight(data)

        return {"type": "sql", "data": data, "insight": insight}

    else:
        data = run_sql_query("sales")
        prediction = predict_sales(data)
        insight = generate_insight(prediction)

        return {"type": "ml", "prediction": prediction, "insight": insight}