import csv
import numpy as np
import plotly.express as px

def getDataSource(data_path):
    marks_percentage = []
    days_attended = []

    with open("marks.csv") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            marks_percentage.append(float(row["Marks In Percentage"]))
            days_attended.append(float(row["Days Present"]))
    
    return {"x":marks_percentage, "y":days_attended}

def findCorrelation(datasource):
    correlation = np.corrcoef(datasource["x"], datasource["y"])
    print("correlation betweeen the marks in percentage and days attended:\n", correlation[0,1] )

def setup():
    data_path = "marks.csv"
    datasource = getDataSource(data_path)
    findCorrelation(datasource)

setup()