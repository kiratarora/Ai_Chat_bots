# Intelligent Bot Suite

This repository contains a suite of intelligent bots designed to interact with users, retrieve information, and answer queries from various sources, including conversation history, online documents, and PDFs. The repository is structured into three main modules, with a simple front-end interface and a Flask server handling backend operations.

## Table of Contents

1. [Modules](#modules)
    - [Conversation Bot](#conversation-bot)
    - [Retrieval Bot](#retrieval-bot)
    - [PDF Bot](#pdf-bot)
2. [Features](#features)
3. [API Usage](#api-usage)
4. [Future Work](#future-work)
5. [Setup and Installation](#setup-and-installation)

## Modules

### 1. Conversation Bot

The Conversation Bot is a simple bot that takes user prompts and fetches answers from OpenAI's GPT-3.5-turbo language model. It uses LangChain to manage conversation history, ensuring content-aware responses. This module includes:

- **Conversation tracking**: Maintains chat history for context-aware responses.
- **LangChain integration**: Uses LangChain for seamless interaction with the language model.

### 2. Retrieval Bot

The Retrieval Bot is designed to access online resources and provide answers by scraping and indexing content. It uses Beautiful Soup for web scraping, Meta's Familiarity Search, and Tavily Search for API integration. This module includes:

- **Web scraping**: Uses Beautiful Soup to scrape content from user-provided URLs.
- **Content indexing**: Indexes scraped content using FAISS vectors.
- **API integration**: Accesses data from APIs using Tavily Search.

### 3. PDF Bot

The PDF Bot loads, indexes, and queries data from PDFs to answer user queries. It leverages LlamaIndex for efficient PDF handling. This module includes:

- **PDF handling**: Accepts and processes PDF files.
- **Data indexing**: Indexes content from PDFs for quick retrieval.
- **Query answering**: Provides answers based on the indexed PDF content.

## Features

- **Front-end**: Simple HTML, CSS, and JavaScript interface for user interaction.
- **Back-end**: Flask server handling requests, storing PDFs, and interacting with the language model.
- **Security**: Chat data is key-encrypted for secure storage.
- **API Access**: Provides an API for using the Conversation Bot programmatically.

## API Usage

Users can interact with the Conversation Bot through an API. The API requires a `chatID` (16-digit integer), a prompt, and an optional chat history. Here's how to use the API:

1. **Endpoint**: `/chat`
2. **Method**: POST
3. **Headers**: 
    - `Content-Type: application/json`
4. **Body**:
    ```json
    {
        "api_key": "your_api_key",
        "chatID": "your_chat_id",
        "prompt": "your_prompt",
    }
    ```
## Future Work

1. **Cloud Hosting**: 
    - **Server Hosting**: Deploy the Flask server on cloud platforms like Render, AWS, or Heroku to make the application accessible online.
    - **Scalability**: Ensure the application can scale to handle multiple users concurrently by leveraging cloud services and load balancers.

2. **Database Integration**: 
    - **File Storage**: Use AWS S3 for storing uploaded PDFs and other files securely.
    - **Database Management**: Implement DynamoDB for managing chat histories and user data to ensure fast and reliable data access.
    
3. **Enhanced Security**: 
    - **Encryption**: Improve encryption mechanisms for stored chat data to enhance security and privacy.
    - **Authentication**: Implement user authentication and authorization to control access to different parts of the application.

4. **API Improvements**: 
    - **Rate Limiting**: Implement rate limiting to prevent abuse of the API.
    - **API Documentation**: Provide comprehensive API documentation using tools like Swagger or Postman to make it easier for developers to use the API.

5. **User Interface Enhancements**: 
    - **Responsive Design**: Improve the front-end design to be fully responsive, ensuring a seamless experience on both desktop and mobile devices.
    - **User Experience**: Add features like chat history search, message timestamps, and improved error handling to enhance the overall user experience.

6. **Advanced Features**: 
    - **Multi-language Support**: Enable support for multiple languages to cater to a wider audience.
    - **Voice Interaction**: Incorporate voice recognition and synthesis to allow users to interact with the bots using voice commands.


## Setup and Installation

1. **Clone the repository**:
    ```sh
    git clone https://github.com/kiratarora/Ai_Chat_bots.git
    cd intelligent-bot-suite
    ```

2. **Set up a virtual environment**:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install the dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

4. **Set up environment variables**:
    - Create a `.env` file and add necessary environment variables (OpenAI API key, and Tavily API key).

5. **Run the Flask server**:
    ```sh
    python conversation_server.py
    ```

6. **Access the front-end**:
    - Open `index.html` in your browser.

## Contribution

Feel free to fork this repository, make enhancements, and create pull requests. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

---

This repository provides a robust foundation for building intelligent conversational bots with advanced retrieval and querying capabilities. Happy coding!


