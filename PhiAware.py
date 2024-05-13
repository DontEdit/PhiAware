from flask import Flask, render_template, request, redirect, url_for, make_response
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///link_clicks.db'
db = SQLAlchemy(app)

class Link(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(200), nullable=False)
    prof_clicks = db.Column(db.Integer, default=0)
    wimi_clicks = db.Column(db.Integer, default=0)
    stud_clicks = db.Column(db.Integer, default=0)

# This function ensures that the application context is set up before creating tables
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    links = Link.query.all()
    return render_template('index.html', links=links)

@app.route('/click/<link_id>/<group>')
def click(link_id, group):
    link = Link.query.get(link_id)
    if group == 'prof':
        link.prof_clicks += 1
    elif group == 'wimi':
        link.wimi_clicks += 1
    elif group == 'stud':
        link.stud_clicks += 1
    db.session.commit()
    response = make_response(redirect(link.url))
    response.set_cookie('clicked_' + link_id, 'true')
    return response

@app.route('/create_link', methods=['POST'])
def create_link():
    url = request.form['url']
    new_link = Link(url=url)
    db.session.add(new_link)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
