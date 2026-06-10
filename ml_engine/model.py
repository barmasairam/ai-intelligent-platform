import pandas as pd
from sklearn.linear_model import LinearRegression

def predict_sales(data):

    df = pd.DataFrame(data)

    # convert date properly
    df['date'] = pd.to_datetime(df['date'])

    # sort by date
    df = df.sort_values('date')

    # create time feature
    df['day'] = (df['date'] - df['date'].min()).dt.days

    X = df[['day']]
    y = df['sales']

    model = LinearRegression()
    model.fit(X, y)

    # predict next 7 days
    future_day = df['day'].max() + 7

    prediction = model.predict([[future_day]])

    return round(float(prediction[0]), 2)