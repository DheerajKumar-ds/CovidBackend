from flask import Flask, render_template, request
from data_processing import fetch_and_process_data
from visualizations import (
    plot_case_density,
    plot_vaccination_completion,
    plot_icu_utilization,
    plot_infection_rate,
    plot_positive_vs_negative_tests,
    plot_beds_in_use,
    plot_vaccines_distributed_vs_administered,
    plot_cumulative_deaths,
    plot_top_deaths,
    plot_top_survival_rate,

)

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def dashboard():
    # Fetch and preprocess data
    data = fetch_and_process_data()

    # Get filter values from the form
    selected_state = request.form.get('state', 'All')  # Default to 'All'

    # Filter data by state if a specific state is selected
    if selected_state != 'All':
        data = data[data['State'] == selected_state]

    # Generate visualizations
    icu_chart = plot_icu_utilization(data)
    infection_rate_chart = plot_infection_rate(data)
    tests_chart = plot_positive_vs_negative_tests(data)
    beds_in_use_chart = plot_beds_in_use(data)
    vaccines_chart = plot_vaccines_distributed_vs_administered(data)
    cumulative_deaths_chart = plot_cumulative_deaths(data)
    top_deaths_chart = plot_top_deaths(data)
    top_survival_rate_chart = plot_top_survival_rate(data)

    # Convert data to HTML table
    table_html = data.to_html(classes='data-table', index=False, border=0)

    # Get unique states for the dropdown
    states = ['All'] + sorted(fetch_and_process_data()['State'].unique())

    # Render the HTML template
    return render_template(
        'index.html',
        tables=table_html,
        states=states,
        selected_state=selected_state,
        icu_chart=icu_chart,
        infection_rate_chart=infection_rate_chart,
        tests_chart=tests_chart,
        beds_in_use_chart=beds_in_use_chart,
        vaccines_chart=vaccines_chart,
        cumulative_deaths_chart=cumulative_deaths_chart,
        top_deaths_chart=top_deaths_chart,
        top_survival_rate_chart=top_survival_rate_chart
    )

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8080)  # Change port to 8080

