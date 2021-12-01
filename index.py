from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/catalogue')
def catalogue():
    return render_template('catalogue.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/closetpill')
def closetpill():
    return render_template('closet-pill.html')

@app.route('/saponifiedsoaps')
def saponifiedsoaps():
    return render_template('saponified-soaps.html')

@app.route('/scentedcandles')
def scentedcandles():
    return render_template('scented-candles.html')

@app.route('/sculpturecandles')
def sculpturecandles():
    return render_template('sculpture-candles.html')

@app.route('/solidshampoo')
def solidshampoo():
    return render_template('solid-shampoo.html')

if __name__ == '__main__':
    app.run(debug=True)
