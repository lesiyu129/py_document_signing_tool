from flask import Flask,request,jsonify
from tool import conversionTools

app = Flask(__name__)

@app.route("/" , methods = ['POST'])
def main():
    if 'file' not in request.files:
        return jsonify({'message':'No file part in the request'}),400
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({'message':'No selected file'}),400
    conversionTools.getFileType()
    
