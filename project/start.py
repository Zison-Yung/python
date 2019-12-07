import os

#设置端口并打开浏览器  默认打开chrome浏览器，端口为localhost:8000
def start(path):
    os.chdir(path)      
    os.system('"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe" http://localhost:8000')  #修改端口和浏览器
    os.system('python -m http.server 8000')  #修改端口

if __name__ == "__main__":
    path = os.getcwd()  #获取当前start.py文件的目录
    start(path)