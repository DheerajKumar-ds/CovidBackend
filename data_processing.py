import requests
import pandas as pd

API_KEY = "71ce39b387c84b9e8a1427bbc62092be"
API_URL = f"https://api.covidactnow.org/v2/states.json?apiKey={API_KEY}"

def fetch_and_process_data():
    # Fetch data from API
    response = requests.get(API_URL)
    data = response.json()

    # Convert JSON to DataFrame
    df = pd.json_normalize(data)

    # Select and rename relevant columns
    df = df[[
        'state',
        'population',
        'lastUpdatedDate',
        'actuals.cases',
        'actuals.deaths',
        'actuals.hospitalBeds.capacity',
        'actuals.hospitalBeds.currentUsageTotal',
        'actuals.icuBeds.capacity',
        'actuals.icuBeds.currentUsageCovid',
        'metrics.bedsWithCovidPatientsRatio',
        'metrics.testPositivityRatio',
        'actuals.vaccinesDistributed',
        'actuals.vaccinesAdministered',
        'actuals.positiveTests',
        'actuals.negativeTests'
    ]]
    df.columns = [
        'State', 'Population', 'LastUpdate', 'Total Cases', 'Total Deaths',
        'Hospital Beds Capacity', 'Current HospBeds Usage', 'ICU Beds Capacity',
        'ICU Beds Usage (COVID)', 'Beds Usage for Covid Ratio',
        'Test Positivity Ratio', 'Vaccines Distributed', 'Vaccines Administered',
        'Positive Tests', 'Negative Tests'
    ]

    # Convert numerical columns to appropriate data types
    numerical_cols = [
        'Population', 'Total Cases', 'Total Deaths',
        'Hospital Beds Capacity', 'Current HospBeds Usage',
        'ICU Beds Capacity', 'ICU Beds Usage (COVID)',
        'Beds Usage for Covid Ratio', 'Test Positivity Ratio',
        'Vaccines Distributed', 'Vaccines Administered',
        'Positive Tests', 'Negative Tests'
    ]
    df[numerical_cols] = df[numerical_cols].apply(pd.to_numeric, errors='coerce')

    # Impute missing values with column means
    df = df.fillna(df.mean(numeric_only=True))

    return df
