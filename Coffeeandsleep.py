import csv
import numpy as np
import plotly.express as px

def getDataSource(data_path):
    coffee_ml = []
    sleep_hours = []

    with open("coffee.csv") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            coffee_ml.append(float(row["Coffee in ml"]))
            sleep_hours.append(float(row["sleep in hours"]))

    return {"x":coffee_ml, "y":sleep_hours}

def findCorrelation(datasource):
    correlation = np.corrcoef(datasource["x"], datasource["y"])
    print("correlation betweeen the amount of coffee drank in ml and the amount of sleep in hours:\n", correlation[0,1] )

def setup():
    data_path = "coffee.csv"
    datasource = getDataSource(data_path)
    findCorrelation(datasource)

setup()