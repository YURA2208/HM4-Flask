from flask import Flask, render_template, request, make_response, session

app = Flask(__name__)
app.secret_key = '22.22.22yura'


@app.route("/")
def index():
    count = 0
    if session.get('visits_count'):
        count = session['visits_count']
    else:
        session['visits_count'] = 0
    response = make_response((render_template('visit_page.html', visits_count=count)))
    session['visits_count'] += 1
    return response



@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return """
        <form action='http://127.0.0.1:5000/login', method='POST'>
            <input name = "username">
            <input type = "submit">
        </form>
        """
    elif request.method == 'POST':
        username = request.form['username']
        response = make_response((render_template('authorisation_page.html', user=username)))
        return response

@app.route("/logout")
def logout():
    visit = "!"
    if 'visits_count' in session:
        session.pop('visit', None)
        response = make_response((render_template('no_visit_page.html', visits_count=visit)))
        return response

if __name__ == "__main__":
    app.run(debug=True)