from flask import Flask, request, jsonify
from conversational_bot import respond_to_prompt
from retrival_bot import start_reterival
from pdf_bot import get_pdf_answers
from flask_cors import CORS, cross_origin
import os

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

UPLOAD_FOLDER = 'data'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/',methods = ['GET'])
@cross_origin()
def hello():
    return 'Hello World!'


@app.route('/chat', methods=['POST'])
@cross_origin()
def chat():
    data = request.json
    chatID = data.get('chatID')
    prompt = data.get('prompt')


    if not prompt:
        return jsonify({"error": "No prompt provided"}), 400

    
    response = respond_to_prompt(chatID, prompt)
    return jsonify({"response": response})

@app.route('/retival', methods=['POST'])
@cross_origin()
def retival():
    data = request.json
    source = data.get('source')
    prompt = data.get('prompt')
    chat_history = data.get('chat_history')


    if not prompt:
        return jsonify({"error": "No prompt provided"}), 400

    
    response = start_reterival(source, chat_history, prompt)
    return jsonify({"response": response})

@app.route('/pdfQuestions', methods=['POST'])
@cross_origin()
def pdfQuestions():
    
    data = request.json
    reload = data.get('reload')
    prompt = data.get('prompt')
    chat_history = data.get('chat_history')


    if not prompt:
        return jsonify({"error": "No prompt provided"}), 400

    
    response = get_pdf_answers(reload, prompt, chat_history)
    return jsonify({"response": response.response})

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    if file and file.filename.endswith('.pdf'):
        file_path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(file_path)
        return jsonify({'success': 'File uploaded successfully'}), 200
    else:
        return jsonify({'error': 'Invalid file type'}), 400


if __name__ == '__main__':
    app.run(debug=True)
