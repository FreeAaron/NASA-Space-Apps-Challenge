from flask import Flask, render_template

app = Flask(__name__,
            static_url_path='', 
            static_folder='Aaron/static/',
            template_folder='Aaron/templates/')

@app.route('/')
@app.route('/index')
def index():
   print('Request for index page received')
   return render_template('index.html')

@app.route("/details")
def details():
    return render_template("portfolio-details.html")

@app.route("/details2")
def details2():
    return render_template("App-details2.html")

@app.route("/details3")
def details3():
    return render_template("App-details3.html")

@app.route("/details4")
def details4():
    return render_template("App-details4.html")

@app.route("/details5")
def details5():
    return render_template("Card-details5.html")

@app.route("/details6")
def details6():
    return render_template("Card-details6.html")

@app.route("/details7")
def details7():
    return render_template("Card-details7.html")

if __name__ == "__main__":
    app.run(debug = True)
