import os
from multiprocessing import Process

'''
设置端口并打开浏览器  默认打开chrome浏览器，端口为localhost:8000
'''
#打开浏览器并进入相应页面
def start_web(path):
    os.chdir(path)   
    os.system('"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe" http://localhost:8000')  #修改端口和浏览器

#创建端口
def start_port():
    os.system('python -m http.server 8000')

if __name__ == "__main__":
    path = os.getcwd()  #获取当前start.py文件的目录
    p1 = Process(target=start_port) #创建端口的进程
    p1.start()
    p2 = Process(target= start_web,args=(path,)) #打开浏览器的进程
    p2.start()