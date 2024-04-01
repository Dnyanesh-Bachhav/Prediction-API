import yfinance as yf
from datetime import datetime
import statsmodels.api as sm
from pytz import timezone
import numpy as np
import pandas as pd



def get_eth():
            ethereum = yf.download("ETH-CAD")
            ethereum = ethereum.drop(columns=['Open','Close','High','Low','Close','Volume'])
            modelhigh = sm.tsa.statespace.SARIMAX(ethereum['Adj Close'],
                                                  order=(0, 1, 1),
                                                  seasonal_order=(1, 1, 1, 12),
                                                  enforce_stationarity=False,
                                                  enforce_invertibility=False)
            resultshigh = modelhigh.fit()
            pred = resultshigh.get_prediction(start=datetime(2018, 11, 11), dynamic=False)
            pred_ci = pred.conf_int()
            pred_uc = resultshigh.get_forecast(steps=30)
            pred_ci = pred_uc.conf_int()
            One_week_values = pred_uc.predicted_mean[:7]
            One_week_values = round(One_week_values, 2)
            
            week_dates = []
            for item in One_week_values.index:
                week_dates.append(item.strftime("%Y-%m-%d"))

            month_dates = []
            for item in pred_uc.predicted_mean.index:
                month_dates.append(item.strftime("%Y-%m-%d"))

            

            data = {
                "one_week_dates":  week_dates,
                "one_week_dollars": One_week_values.values,
                "one_month_dates": month_dates,
                "one_month_dollars": pred_uc.predicted_mean.values
            }


            return data