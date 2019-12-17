import os
from multiprocessing import Process

#设置端口并打开浏览器  默认打开chrome浏览器，端口为localhost:8000
def start_web(path):
    os.chdir(path)   
    os.system('"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe" http://localhost:8000')  #修改端口和浏览器
    #os.system('python -m http.server 8000')  #修改端口

def start_port():
    os.system('python -m http.server 8000')

if __name__ == "__main__":
    path = os.getcwd()  #获取当前start.py文件的目录
    #start(path)
    p1 = Process(target=start_port)
    p1.start()
    p2 = Process(target= start_web,args=(path,))
    p2.start()