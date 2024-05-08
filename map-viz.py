from flask import Flask, render_template, request, jsonify
import pandas as pd
import plotly.express as px
import json
import plotly
import os
import us

app = Flask(__name__)

def load_data():
    file_path = os.path.join(os.path.dirname(__file__), 'commercial-backyard-flocks.csv')
    data = pd.read_csv(file_path, parse_dates=['Outbreak Date'], dayfirst=False, infer_datetime_format=True)
    data['Year'] = data['Outbreak Date'].dt.year
    data['State Code'] = data['State'].apply(lambda x: us.states.lookup(x).abbr if us.states.lookup(x) else None)
    return data

data = load_data()

def sum_infections():
    total_infections = data['Flock Size'].sum()
    data_by_state = data.groupby('State Code')['Flock Size'].sum().to_dict()
    cumulative_data_by_year = data.groupby('Year')['Flock Size'].sum().cumsum().to_dict()  # Calculating cumulative data
    return total_infections, data_by_state, cumulative_data_by_year

data_summary = sum_infections()
total_infections = data_summary[0]
infections_by_state = data_summary[1]
cumulative_infections_by_year = data_summary[2]  # Updated to cumulative data

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calculate-total-infections')
def calculate_total_infections():
    return jsonify(total_infections=int(total_infections))

@app.route('/infections-by-location')
def infections_by_location():
    state_code = request.args.get('state', '').upper()
    count = infections_by_state.get(state_code, 0)
    return jsonify(infections_by_location=count)

@app.route('/infections-by-time')
def infections_by_time():
    year = request.args.get('year', '')
    count = cumulative_infections_by_year.get(int(year), 0) if year.isdigit() else 0
    return jsonify(infections_by_time=count)  # Now returns cumulative counts

@app.route('/state-infections')
def state_infections():
    fig = px.bar(data.groupby('State Code')['Flock Size'].sum().reset_index(),
                 x='State Code', y='Flock Size', title='Infections by State',
                 labels={'Flock Size': 'Total Infections'})
    graph_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return render_template('plot.html', plot=graph_json)

@app.route('/time-series')
def time_series():
    cumulative_data = data.groupby('Year')['Flock Size'].sum().cumsum().reset_index()
    fig = px.line(cumulative_data,
                  x='Year', y='Flock Size', title='Cumulative Infections Over Time',
                  labels={'Flock Size': 'Cumulative Infections'})
    fig.update_layout(xaxis=dict(tickmode='linear', tick0=data['Year'].min(), dtick=1))
    graph_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return render_template('plot.html', plot=graph_json)

@app.route('/us-map')
def us_map():
    state_data = data.groupby('State Code')['Flock Size'].sum().reset_index()
    fig = px.choropleth(state_data,
                        locations='State Code',
                        locationmode='USA-states',
                        color='Flock Size',
                        scope="usa",
                        title="Infections by State on US Map",
                        labels={'Flock Size': 'Total Infections'},
                        color_continuous_scale="Viridis")
    graph_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return render_template('plot.html', plot=graph_json)

if __name__ == '__main__':
    app.run(debug=True)
