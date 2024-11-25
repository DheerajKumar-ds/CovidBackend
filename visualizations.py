import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import os

os.makedirs('static', exist_ok=True)

# Static Visualization: Top 10 States by Case Density
def plot_case_density(data):
    top_states = data.nlargest(10, 'Total Cases')
    plt.figure(figsize=(10, 6))
    sns.barplot(data=top_states, x='State', y='Total Cases', palette='Reds')
    plt.title('Top 10 States by Total Cases')
    plt.xlabel('State')
    plt.ylabel('Total Cases')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('static/case_density.png')
    plt.close()

#Top 10 states by death
def plot_top_deaths(data):
    top_states = data.nlargest(10, 'Total Deaths')
    fig = px.bar(
        top_states,
        x='State',
        y='Total Deaths',
        title='Top 10 States by Deaths',
        labels={'Total Deaths': 'Deaths'},
        color='Total Deaths',
        color_continuous_scale='Reds'
    )
    return fig.to_html(full_html=False)

#Top 10 States by Survival Rate
def plot_top_survival_rate(data):
    data['Survival Rate (%)'] = ((data['Population'] - data['Total Deaths']) / data['Population']) * 100
    top_states = data.nlargest(10, 'Survival Rate (%)')
    fig = px.bar(
        top_states,
        x='State',
        y='Survival Rate (%)',
        title='Top 10 States by Survival Rate (%)',
        labels={'Survival Rate (%)': 'Survival Rate (%)'},
        color='Survival Rate (%)',
        color_continuous_scale='Greens'
    )
    return fig.to_html(full_html=False)

# Static Visualization: Top 10 States by Vaccination Completion
def plot_vaccination_completion(data):
    data['Vaccination Completion Rate (%)'] = (data['Vaccines Administered'] / data['Population']) * 100
    top_states = data.nlargest(10, 'Vaccination Completion Rate (%)')
    plt.figure(figsize=(10, 6))
    sns.barplot(data=top_states, x='State', y='Vaccination Completion Rate (%)', palette='Greens')
    plt.title('Top 10 States by Vaccination Completion Rate (%)')
    plt.xlabel('State')
    plt.ylabel('Completion Rate (%)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('static/vaccination_completion.png')
    plt.close()

# Interactive Visualization: ICU Utilization
def plot_icu_utilization(data):
    fig = px.bar(
        data,
        x='State',
        y=['ICU Beds Capacity', 'ICU Beds Usage (COVID)'],
        title='ICU Bed Utilization by State',
        labels={'value': 'Beds (in Thousands)', 'variable': 'Metric'},
        barmode='group',
        color_discrete_sequence=['#636EFA', '#EF553B']
    )
    return fig.to_html(full_html=False)

# Interactive Visualization: Infection Rate
def plot_infection_rate(data):
    data['Infection Rate (%)'] = (data['Total Cases'] / data['Population']) * 100
    top_states = data.nlargest(10, 'Infection Rate (%)')
    fig = px.bar(
        top_states,
        x='State',
        y='Infection Rate (%)',
        title='Top 10 States by Infection Rate (%)',
        labels={'Infection Rate (%)': 'Infection Rate (%)'},
        color='Infection Rate (%)',
        color_continuous_scale='Oranges'
    )
    return fig.to_html(full_html=False)

# Interactive Visualization: Positive vs. Negative Tests
def plot_positive_vs_negative_tests(data):
    top_states = data.nlargest(10, 'Positive Tests')
    fig = px.bar(
        top_states,
        x='State',
        y=['Positive Tests', 'Negative Tests'],
        title='Positive vs Negative Tests by State',
        labels={'value': 'Tests', 'variable': 'Test Type'},
        barmode='group',
        color_discrete_sequence=['#EF553B', '#636EFA']
    )
    return fig.to_html(full_html=False)

# Interactive Visualization: Beds in Use by COVID Patients vs Total Beds
def plot_beds_in_use(data):
    top_states = data.nlargest(10, 'Hospital Beds Capacity')
    fig = px.bar(
        top_states,
        x='State',
        y=['Hospital Beds Capacity', 'Current HospBeds Usage'],
        title='Beds in Use by COVID Patients vs Total Beds',
        labels={'value': 'Beds', 'variable': 'Type'},
        barmode='group',
        color_discrete_sequence=['#636EFA', '#EF553B']
    )
    return fig.to_html(full_html=False)

# Interactive Visualization: Vaccines Distributed vs Administered
def plot_vaccines_distributed_vs_administered(data):
    top_states = data.nlargest(10, 'Vaccines Distributed')
    fig = px.bar(
        top_states,
        x='State',
        y=['Vaccines Distributed', 'Vaccines Administered'],
        title='Vaccines Distributed vs Administered',
        labels={'value': 'Vaccines', 'variable': 'Type'},
        barmode='group',
        color_discrete_sequence=['#00CC96', '#FFA15A']
    )
    return fig.to_html(full_html=False)

# Interactive Visualization: Cumulative Deaths
def plot_cumulative_deaths(data):
    cumulative_deaths = data['Total Deaths'].sum()
    fig = px.pie(
        values=[cumulative_deaths, data['Population'].sum() - cumulative_deaths],
        names=['Cumulative Deaths', 'Surviving Population'],
        title='Cumulative Deaths vs Surviving Population',
        color_discrete_sequence=['#EF553B', '#00CC96']
    )
    return fig.to_html(full_html=False)
