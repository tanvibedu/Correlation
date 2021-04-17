import plotly.express as px
import csv

with open("./Ice-Cream vs Cold-Drink vs Temperature - Ice Cream Sale vs Temperature data.csv") as csv_file:
      df = csv.DictReader(csv_file)
      fig = px.scatter(df,x="Cold drink sales( ₹ )", y="Ice-cream Sales( ₹ )", color= "Temperature")
      fig.show()