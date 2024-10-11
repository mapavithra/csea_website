from flask import Flask, render_template

app = Flask(__name__)

# Home page route
@app.route('/')
def home():
    return render_template('index.html')

# About page route
@app.route('/about')
def about():
    return render_template('about.html')

# Announcements page route
@app.route('/announcements')
def announcements():
    events = [
        {"title": "Coding Hackathon", "date": "2024-10-15", "details": "A 24-hour coding challenge..."},
        {"title": "Workshop on AI", "date": "2024-11-01", "details": "Learn the basics of AI and ML..."}
    ]
    return render_template('announcements.html', events=events)

# Winners announcement route
@app.route('/winners')
def winners():
    winners_list = [
        {"event": "Hackathon", "name": "John Doe", "position": 1},
        {"event": "Quiz", "name": "Jane Smith", "position": 2}
    ]
    return render_template('winners.html', winners=winners_list)

# Scoreboard route
@app.route('/scoreboard')
def scoreboard():
    scores = [
        {"team": "Team A", "score": 95},
        {"team": "Team B", "score": 88}
    ]
    return render_template('scoreboard.html', scores=scores)

# Photo gallery route
@app.route('/gallery')
def gallery():
    photos = ["image1.jpg", "image2.jpg", "image3.jpg"]
    return render_template('gallery.html', photos=photos)

# Office bearers route
@app.route('/office-bearers')
def office_bearers():
    bearers = [
        {"name": "Alice Johnson", "position": "President"},
        {"name": "Bob Williams", "position": "Vice President"},
        {"name": "Charlie Brown", "position": "Secretary"}
    ]
    return render_template('office_bearers.html', bearers=bearers)

if __name__ == "__main__":
    app.run(debug=True)
