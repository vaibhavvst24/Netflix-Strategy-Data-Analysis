from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    plots = [
        {
            'title': 'Average Hours Viewed by Global Availability',
            'description': 'Compares average viewing hours between content available globally and region-specific releases.',
            'file': 'Average Hours Viewed by Gloabal Availability.html'
        },
        {
            'title': 'Total Hours Viewed by Content Type',
            'description': 'Shows the overall viewing time for Movies and TV Shows, highlighting which content type drives more audience engagement.',
            'file': 'Total Hours Viewed by Content type.html'
        },
        {
            'title': 'Most Watched Languages on Netflix',
            'description': 'Displays the top-performing languages based on total viewing hours, revealing audience language preferences.',
            'file': 'Most Watch Language.html'
        },
        {
            'title': 'Average Hours Viewed by Release Year',
            'description': 'Tracks how viewer engagement has changed across different release years to identify content popularity trends.',
            'file': 'Average Hours View by Release.html'
        },
        {
            'title': 'Distribution of Content Type',
            'description': 'Visualizes the share of Movies and TV Shows on Netflix, showing the platform’s focus across content categories.',
            'file': 'Distribution of Content Type.html'
        },
        {
            'title': 'Monthly Release Patterns & Viewership',
            'description': 'Highlights which months see the highest number of releases and viewership, revealing seasonal content trends.',
            'file': 'Monthly Release Patterns & Viewership.html'
        },
        {
            'title': 'Netflix Global Availability',
            'description': 'Illustrates the proportion of titles available worldwide versus region-specific, reflecting Netflix’s global reach.',
            'file': 'Netflix Global Availability.html'
        },
        {
            'title': 'Number of Netflix Release over Years',
            'description': 'Shows the growth trend in Netflix releases across years, indicating the platform’s expansion strategy.',
            'file': 'Number of Netflix Release over Years.html'
        },
        {
            'title': 'Top 10 Languages on Netflix',
            'description': 'Lists the most common languages used in Netflix titles, reflecting linguistic diversity in its catalog.',
            'file': 'Top 10 Languages on Netflix.html'
        },
        {
            'title': 'Average Hours View by Release',
            'description': 'Examines the relationship between release timing and average viewership to identify performance trends of new content.',
            'file': 'Average Hours View by Release.html'
        },
        {
            'title': 'Viewership Hours by Language',
            'description': 'Compares total viewing hours across different languages to reveal audience preferences and dominant regions.',
            'file': 'Viewership Hours by Language.html'
        },
        {
            'title': 'Viewership Hours by Release Month',
            'description': 'Highlights how viewing activity varies by month, uncovering seasonal spikes in Netflix engagement.',
            'file': 'Viewership Hours by Release Month.html'
        },
        {
            'title': 'Viewership Hours by season 2023',
            'description': 'Analyzes content performance across the four seasons of 2023 to identify when audiences were most active.',
            'file': 'Viewership Hours by season 2023.html'
        },
        {
            'title': 'Viewership Hours',
            'description': 'Displays the overall distribution of viewing hours, showing how much content is being consumed globally.',
            'file': 'Viewership Hours.html'
        },
        {
            'title': 'Viewership Trends by Content',
            'description': 'Tracks changing audience engagement between Movies and TV Shows over time to reveal viewing patterns.',
            'file': 'Viewership Trends by Content.html'
        },
        {
            'title': 'Weekly Release Patterns & Hours',
            'description': 'Shows how Netflix’s weekly release schedule impacts total viewing hours, highlighting peak engagement days.',
            'file': 'Weekly Release Patterns & Hours.html'
        },
    ]
    return render_template('index.html', plots=plots)

if __name__ == '__main__':
    app.run(debug=True)
