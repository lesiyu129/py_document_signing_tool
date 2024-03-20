from flask import Flask,request,jsonify
from tool import conversionTools
import uuid
import os
app = Flask(__name__)

@app.route("/" , methods = ['POST'])
def main():
    if 'file' not in request.files:
        return jsonify({'message':'No file part in the request'}),400
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({'message':'No selected file'}),400
    filePath = './files'
    if os.path.exists(filePath) and os.path.isdir(filePath):
        pass
    else:    
        os.mkdir('./files')
        
    uid = uuid.uuid4()
    fileType = conversionTools.getFileType(file.filename)
    newFileName = f'{uid}.{fileType}'
    newFilePath = f'./files/{newFileName}'
    file.save(newFilePath)
    return 'OK',200
    
