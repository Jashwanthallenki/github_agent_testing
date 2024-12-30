from flask import Flask

# Initialize the Flask app
app = Flask(__name__)

# Define a route for the homepage
@app.route('/')
def home():
    return "Hello, Welcome to Flask!"

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
