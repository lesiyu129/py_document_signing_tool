from enum import Enum
import subprocess
import os  
class __DocumentType(Enum):
    DOCX = 'docx'
    XLSX = 'xlsx'

# 文档转换工具
def __conversionTools(input_file,output_file,type):
    if(__is_libreoffice_installed==False):
        print('系统没有安装libreoffice')
        raise FileNotFoundError('系统中没有找到libreoffice请自行安装')
    command = ['libreoffice','--headless','--convert-to',format,'--outdir',output_file,input_file]
    subprocess.run(command,check=True)
    file = os.path.basename(input_file)
    fileName = os.path.splitext(file)[0]
    converted_file = fileName+'.'+type
    return converted_file

#doc转docx
def docToDocx(input_file: str,output_file: str) -> str:
    """doc转换成docx

    Args:
        input_file (str): 输入文件
        output_file (str): 输出文件
    Returns:
        str: 返回转换后的文件名称
    """
    return __conversionTools(input_file,output_file,__DocumentType.DOCX)

#xls转xls
def xlsToXlsx(input_file: str,output_file: str) -> str:
    """xls转换成xlsx

    Args:
        input_file (str): 输入文件
        output_file (str): 输出文件

    Returns:
        str: 返回转换后的文件名称
    """
    return __conversionTools(input_file,output_file,__DocumentType.XLSX)

#文件类型获取
def getFileType(fileName: str) -> str:
    """获取文件类型

    Args:
        fileName (str): 文件路径

    Returns:
        str: 返回文件扩展名
    """
    return os.path.splitext(fileName)[1][1:].lower()  # [1:] 是为了移除扩展名前的'.'  

# 环境监测工具
def __is_libreoffice_installed():
    commands = ['libreoffice', 'soffice']  
    
    for cmd in commands:
        try:
            # 检查命令是否存在并可执行  
            subprocess.run([cmd, '--version'], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)  
            return True  
        except FileNotFoundError:
            pass
        
    return False
