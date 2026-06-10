def route_query(query):

    q = query.lower()

    if "predict" in q or "forecast" in q:
        return "ml"

    return "sql"