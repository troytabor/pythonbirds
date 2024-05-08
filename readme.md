# Bird Infections Data Visualization and Analysis Tool

## Overview

This tool provides a visualization of initial outbreak records of bird infections across the US, based on reported flock sizes and outbreak dates. It includes a series of interactive maps and graphs to help understand the spread and intensity of the outbreaks over time.

## Components

setup.py: Script to set up the Python virtual environment and install necessary packages.

map-viz.py: Flask application that provides web-based visualizations of the data on a US map.

## Setup Instructions

Create a Virtual Environment and Install Dependencies:
Ensure Python is installed on your system, then run the following command to set up the environment:

```python setup.py```

Some installations require that RUST needs to be installed, and if you get an error when running setup.py, go to https://rustup.rs/ and follow the instructions to install on your system. You will see in Windows that you need to allow it to install. Then run ```python setup.py``` again

## Data Preparation:
Ensure the data file commercial-backyard-flocks.csv is placed in the same directory as the Flask application scripts. The data should include columns for 'Outbreak Date' and 'Flock Size'.

## Run the Application:
To start the server, navigate to the directory containing map-viz.py and run:

```python map-viz.py```


## Access the Web Interface:
Open a web browser and go to http://localhost:5000 (Shown in terminal, subject to address change) to view the application. You can cmd click the address in the terminal if you are on macOS, or ctrl click the the address if on Windows.

## Interacting with Visualizations:
Use the links provided on the homepage to navigate between different visualizations:

**Total Infections**: Summarizes the total infections recorded at the time of the outbreak.

**Infections by State**: Visualizes the number of infections per state on a bar graph.

**Infections Over Time**: Displays a line graph showing how recorded infections have changed over the years.

**US Map**: Shows a choropleth map of the US with states colored based on the infection intensity.

**Calculating Infections**: Use the input fields and buttons on the homepage to calculate total infections, infections by location (state), and infections by time (year).

### Libraries Used

  *Flask*: Web framework for serving the application.
  
  *Pandas*: Data manipulation and analysis.
  
  *Plotly*: Creating interactive charts and maps.
  
### File Descriptions

*setup.py*: Initializes the virtual environment and installs dependencies.

*map-viz.py*: Main Flask application script for rendering the web pages and handling data processing.

*index.html*: Frontend HTML template for the homepage of the web application.

*plot.html*: Template for rendering Plotly graphs within the Flask app.

*main.js*: Frontend JavaScript for handling user interactions and data updates.


### Developer Notes

Ensure that the CSV data is formatted correctly and the Flask server is configured to allow sufficient resources for data processing and visualization.
For deployment or production use, consider configuring the Flask application with a production-grade server like Gunicorn and setting up an HTTPS proxy with Nginx.
