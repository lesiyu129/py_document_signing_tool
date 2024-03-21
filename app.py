from flask import Flask,request,jsonify
from tool import conversionTools
import uuid
import os
app = Flask(__name__)

@app.route("/" , methods = ['POST'])
def main():
    # 文档转换开始
    if 'file' not in request.files:
        return jsonify({'message':'No file part in the request'}),400
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({'message':'No selected file'}),400
    filePath = './files'
    mkdirPath(filePath)   
    uid = uuid.uuid4()
    fileType = conversionTools.getFileType(file.filename)
    newFileName = f'{uid}.{fileType}'
    newFilePath = f'./files/{newFileName}'
    file.save(newFilePath)
    switch_dist = {
        'doc':conversionTools.docToDocx,
        'xls':conversionTools.xlsToXlsx
    }
    if fileType in switch_dist:
        newConvertFileName = switch_dist[fileType](newFilePath,'./files')
        os.remove(newFilePath)
        newFilePath = f'./files/{newConvertFileName}'
    else:
        pass
    # 文档转换结束
    # 文档签名开始
    
    # 文档签名结束
    
    
    return jsonify({'message':'OK'}),200
    
def mkdirPath(filePath):
    if os.path.exists(filePath) and os.path.isdir(filePath):
        pass
    else:    
        os.mkdir(filePath)