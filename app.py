from flask import Flask, render_template

# app = Flask(__name__,
#             static_url_path='', 
#             static_folder='app/static/',
#             template_folder='app/templates/')

app = Flask(__name__,
            static_url_path="/", 
            static_folder='BS5/static/',
            template_folder='BS5/templates/')

@app.route('/')
def index():
   print('Request for index page received')
   return render_template('index.html')

if __name__ == "__main__":
    app.run()
