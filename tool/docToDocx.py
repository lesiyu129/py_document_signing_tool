import subprocess
import os  
def docToDocx(input_file,output_file,format):
    if(is_libreoffice_installed==False):
        print('系统没有安装libreoffice')
        raise FileNotFoundError('系统中没有找到libreoffice请自行安装')
    command = ['libreoffice','--headless','--convert-to',format,'--outdir',output_file,input_file]
    subprocess.run(command,check=True)
    file = os.path.basename(input_file)
    fileName = os.path.splitext(file)[0]
    converted_file = fileName + '.docx'  
    return converted_file
 

def is_libreoffice_installed():
    commands = ['libreoffice', 'soffice']  
    
    for cmd in commands:
        try:
            # 检查命令是否存在并可执行  
            subprocess.run([cmd, '--version'], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)  
            return True  
        except FileNotFoundError:
            pass
        
    return False

if __name__ == '__main__':
    input_file = './fileTest/docTest.doc'
    output_file='./fileTest/'
    format = 'docx'
    docToDocx(input_file,output_file,format)