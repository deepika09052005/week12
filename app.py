from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('register.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['username']
    return render_template('greeting.html', name=name)

if __name__ == '__main__':
    app.run(debug=True)