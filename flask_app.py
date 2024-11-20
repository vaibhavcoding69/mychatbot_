from flask import Flask, request, render_template
from chatbot import process_user_input


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def chatbot():
    """
    This function handles the main logic of the chatbot. It processes user input and generates a response.

    Parameters:
    - request: The Flask request object containing information about the incoming HTTP request.

    Returns:
    - If the request method is POST, it retrieves the user input from the request form, processes it using the
      `process_user_input` function, and returns the response.
    - If the request method is GET, it renders the HTML code for the chatbot interface.
    """

    if request.method == 'POST':
        user_input = request.form.get('user_input')
        response = process_user_input(user_input)
        return response

    # Render the HTML template for the chatbot interface
    return render_template('base.html')


if __name__ == '__main__':
    app.run(debug=True)