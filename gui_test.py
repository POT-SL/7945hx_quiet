from webui import webui
from flask import Flask, send_from_directory, request, send_file
from json import loads
from threading import Thread
from multiprocessing import Process

app = Flask(__name__, static_url_path='', static_folder='./gui')
########################################################################################################################
#
# 事件处理
#

#############
# 处理主程序 #
###########
@app.route('/send', methods=['POST'])
def send_process():
    data = loads(request.get_data().decode('utf-8'))
    print(data)
    return 'ok'
########################################################################################################################
#
# GUI部分
#

#############
# flaskGUI #
###########
def gui_flask():

    @app.route('/')
    def index():
        return send_from_directory('./GUI', 'index.html')
    app.run(host='0.0.0.0', port=541)

##############
# webGUI框架 #
#############
def gui_web():
    my_window = webui.window(1)
    my_window.set_size(800, 540)
    webui.set_timeout(0)
    my_window.show('http://localhost:541/')
    print(1)
########################################################################################################################
def main():
    Process(target=gui_flask).start()
    Thread(target=gui_web).start()

if __name__ == '__main__':
    main()