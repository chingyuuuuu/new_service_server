from flask import Blueprint, jsonify,send_from_directory,redirect
from sqlalchemy.exc import OperationalError
from sqlalchemy.sql import text
from flask_mail import Message
import os



main_routes = Blueprint('main_routes', __name__)


@main_routes.route('/api/data')
def get_data():
    return jsonify({'message': 'Hello from Flask!'})


@main_routes.route('/')
def server_web():
    static_folder = os.path.join(os.getcwd(), 'my_flask_app', 'static')
    return send_from_directory(static_folder,'index.html')

@main_routes.route('/<path:path>')
def serve_static_flies(path):
    static_folder = os.path.join(os.getcwd(), 'my_flask_app', 'static')
    # 如果請求的文件存在於靜態文件夾中，則返回該文件
    if os.path.exists(os.path.join(static_folder, path)):
        return send_from_directory(static_folder, path)

    # 否則返回 index.html，交由前端處理路由
    return send_from_directory(static_folder, 'index.html')


@main_routes.route('/home')
def home():
    return 'Welcome to the home page!'


@main_routes.route('/test_db', methods=['GET'])
def test_db():
    from .. import db
    try:
        db.session.execute(text('SELECT 1'))
        return 'Database connection is successful!', 200
    except OperationalError as e:
        print(f"Database connection failed: {e}")
        return f'Database connection failed! {str(e)}', 500


@main_routes.route('/send_email')
def send_email():
    from .. import mail
    msg = Message('Hello', sender='your_email@gmail.com', recipients=['recipient@example.com'])
    msg.body = 'This is a test email.'
    try:
        mail.send(msg)
        return 'Email sent!'
    except Exception as e:
        return f'Failed to send email: {e}'

