from flask import Flask, render_template

# app = Flask(__name__,
#             static_url_path='', 
#             static_folder='app/static/',
#             template_folder='app/templates/')

# app = Flask(__name__,
#             static_url_path="/", 
#             static_folder='BS5/static/',
#             template_folder='BS5/templates/')

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

if __name__ == "__main__":
    app.run(debug = True)
