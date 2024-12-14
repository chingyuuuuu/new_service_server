from flask import Flask
from flask_cors import CORS
from my_flask_app.app.routes.main_route import main_routes
from .config import Config
from flask_mail import Mail
from .routes import auth_routes, product_routes, order_routes, main_route,QA_routes
from .extensions import db
from flask_socketio import SocketIO

mail = Mail()
socketio = SocketIO(cors_allowed_origins="*")  # WebSocket 配置


#定義create_app
def create_app():   # 配置flask
    app = Flask(__name__)   # 創建flask實例
    app.config['DEBUG'] = True  # 開啟 Debug 模式
    app.config.from_object("my_flask_app.app.config.Config")
    CORS(app)
    #初始化擴展
    db.init_app(app)
    mail.init_app(app)
    #註冊藍圖
    app.register_blueprint(main_routes)
    app.register_blueprint(product_routes)
    app.register_blueprint(auth_routes)
    app.register_blueprint(order_routes)
    app.register_blueprint(QA_routes)
    socketio.init_app(app)#將socketio綁訂到flask應用中    from .websocket_handlers import handle_connect, handle_disconnect, handle_client_message

    return app
