#flask , scikit_learn, pandas, pickle_mixing

from flask import Flask, render_template
import pandas as pd
#Create a flask object
app = Flask(__name__)
#laod cleaned dataset
car= pd.read_csv("cleaned_Car.csv")
#create a route at entry point of our application
@app.route('/')

#define Index(when someone will hit our router(simply call something))
def index():
    companies = sorted(car["company"].unique())
    car_models = sorted(car["name"].unique())
    year = sorted(car["year"].unique(), reverse = True)
    fuel_type = sorted(car["fuel_type"].unique())
    return render_template('index.html', companies= companies, car_models= car_models, years= year, fuel_type=fuel_type)

if __name__ == "__main__":
    app.run(debug=True)



