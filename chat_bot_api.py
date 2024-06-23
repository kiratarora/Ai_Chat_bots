import requests
import json

def chat(id, question):
    """
    This function is used to chat with the LLM maintaining the chat history.
    In its current form, the user needs to maintain and pass the chat history themselves,
    but in a later update, the user will only need to pass the chat_id.
    """
    
    # Create the message payload
    message = {
        "chatID": id,
        "prompt": question,
    }

    # Send the POST request to the Flask server
    response = requests.post('http://127.0.0.1:5000/chat', 
                             headers={'Content-Type': 'application/json'},
                             data=json.dumps(message))
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the response JSON
        result = response.json()
        return result['response']
    else:
        # Handle the error
        print(f"Error: {response.status_code}")
        print(response.text)
        return None

# Example usage
if __name__ == '__main__':
    chat_id = 1234567890123456
    question = "What was my previous question?"
    
    response = chat(chat_id, question)
    if response:
        print("AI response:", response)
