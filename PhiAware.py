from flask import Flask, render_template, request, redirect, url_for, make_response
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///link_clicks.db'
db = SQLAlchemy(app)

class Click(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    group = db.Column(db.String(10), nullable=False)
    count = db.Column(db.Integer, default=0)

# This function ensures that the application context is set up before creating tables
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<group>/<path:url>')
def click(group, url):
    if group in ['prof', 'wimi', 'stud']:
        # Check if the link has been clicked in this session for this group
        if 'clicked_' + url + '_' + group not in request.cookies:
            # Get the click record for the group
            click_record = Click.query.filter_by(group=group).first()
            if not click_record:
                # If the record doesn't exist, create a new one
                click_record = Click(group=group, count=0)
                db.session.add(click_record)
            click_record.count += 1
            db.session.commit()
            
            response = make_response(redirect(url))
            # Set a cookie to mark that this link has been clicked for this group
            response.set_cookie('clicked_' + url + '_' + group, 'true')
            return response
        else:
            print("You've already clicked this link for this group.")
            return redirect(url_for('index'))
    else:
        print("Invalid group.")
        return redirect(url_for('index'))

# Route for any other page
@app.route('/<path:path>')
def other_page(path):
    # Redirect to the index page
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
