import google.generativeai as ai

API_KEY = "AIzaSyBfB2H8PXphoHntpYlJKsRihZLXLXNuMIM"

ai.configure(api_key=API_KEY)

model = ai.GenerativeModel("gemini-pro")
chat = model.start_chat()

def process_user_input(user_input):
    response = chat.send_message(user_input)
    formatted_response = ""

    # Split the response into lines
    lines = response.text.split("\n")

    for line in lines:
        # Check if the line starts with an asterisk (*) for italic
        if line.startswith("*"):
            formatted_line = f"<i>{line[1:]}</i>"
        # Check if the line starts with double asterisks (**) for bold
        elif line.startswith("**"):
            formatted_line = f"<b>{line[2:]}</b>"
        else:
            formatted_line = line

        # Add a new line before the formatted line
        formatted_response += f"<p>{formatted_line}</p>"

    return formatted_response