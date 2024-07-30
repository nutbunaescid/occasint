   from flask import Flask, jsonify, request

   app = Flask(__name__)

   # Define a route for the home page
   @app.route('/')
   def home():
       return "Welcome to the Flask Web Server!"

   # Define a route to return a JSON response
   @app.route('/api/data', methods=['GET'])
   def get_data():
       data = {
           'name': 'John Doe',
           'email': 'john.doe@example.com'
       }
       return jsonify(data)

   # Define a route to handle POST requests with JSON payload
   @app.route('/api/data', methods=['POST'])
   def create_data():
       new_data = request.get_json()
       response = {
           'message': 'Data received',
           'received_data': new_data
       }
       return jsonify(response), 201

   if __name__ == '__main__':
       app.run(debug=True)
   