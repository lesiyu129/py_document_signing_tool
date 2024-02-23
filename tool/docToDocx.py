import subprocess
import os  
def docToDocx(input_file,output_file):
    command = ['unoconv','-f','docx',input_file]
    subprocess.run(command,check=True)
    file = os.path.basename(input_file)
    fileName = os.path.splitext(file)[0]
    converted_file = fileName + '.docx'  
    subprocess.run([])