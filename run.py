from ChatbotWebsite import create_app, mongo  # Import the mongo instance directly
from flask import render_template
# Create the app
app = create_app()  # This creates the app instance

@app.route('/test_db')
def test_db():
    try:
        mongo.db.users.find_one()  # Replace with your actual collection name
        return "MongoDB connection is successful!"
    except Exception as e:
        return f"Error connecting to MongoDB: {e}"


# Run the app
if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)
