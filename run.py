from gevent import pywsgi
from geventwebsocket.handler import WebSocketHandler
from my_flask_app.app import create_app

app = create_app()

if __name__ == '__main__':
    # 使用 gevent 的 WSGI 服務器
    print("Starting server on http://140.136.151.74:5000/")
    server = pywsgi.WSGIServer( ('0.0.0.0', 5000), app, handler_class=WebSocketHandler)
    server.serve_forever()  # 啟動服務器
