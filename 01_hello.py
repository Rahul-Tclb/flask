from flask import Flask

# An object of Flask class is our WSGI application. 
app = Flask(__name__)


# The route() function of the Flask class tells the application which URL should call the associated function.
@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__=="__main__":
    # run() method of Flask class runs the application on the local development server.
    app.run(host="0.0.0.0", port=1234, debug=True)


# Ref: 
#   https://www.tutorialspoint.com/