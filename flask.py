from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    netflix_info = {
        'name': 'Netflix',
        'launch_year': 1997,
        'founders': 'Reed Hastings, Marc Randolph',
        'headquarters': 'Los Gatos, California, United States',
        'services': [
            'Streaming movies and TV shows',
            'Original content production',
            'Subscription-based service'
        ],
        'popular_shows': [
            'Stranger Things',
            'The Witcher',
            'Bridgerton',
            'Money Heist'
        ]
    }

    return render_template('index.html', netflix_info=netflix_info)

if __name__ == "__main__":
    app.run(debug=True)
