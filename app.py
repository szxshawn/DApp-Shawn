from flask import Flask,render_template,request
import sqlite3
import datetime
from flask import Flask, render_template, request, redirect, url_for,session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

# app=Flask(__name__)
# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     wallet_address = db.Column(db.String(80), unique=True, nullable=False)
#     password = db.Column(db.String(120), nullable=False)

#     def __repr__(self):
#         return f'<User {self.wallet_address}>'


# @app.route('/',methods=["get","post"])
# def index():
#     return render_template('index.html')


# @app.route('/register', methods=['GET', 'POST'])
# def register():
#     if request.method == 'POST':
#         wallet_address = request.form['wallet_address']
#         password = request.form['password']
        
#         # 检查用户是否已存在
#         existing_user = User.query.filter_by(wallet_address=wallet_address).first()
#         if existing_user:
#             msg = "User already exists! Try another username!"
#             return render_template('register.html', message=msg)

#         # 创建新用户
#         new_user = User(wallet_address=wallet_address, password=password)
#         try:
#             db.session.add(new_user)
#             db.session.commit()
#         except:
#             msg = "There was an issue adding your account. Please try again."
#             return render_template('register.html', message=msg)

#         return redirect(url_for('login'))
    
#     # GET 请求，显示注册页面
#     return render_template('register.html')
# #########################################################################################################################
# # 初始化Flask应用
# app = Flask(__name__)

# # 配置SECRET_KEY和数据库URI，指定数据库路径
# app.config['SECRET_KEY'] = 'your_secret_key'  # 设置SECRET_KEY
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///account.db'  # 或者使用 'sqlite:///database/account.db' 指定路径

# # 初始化数据库
# db = SQLAlchemy(app)

# # 定义User模型
# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     wallet_address = db.Column(db.String(80), unique=True, nullable=False)
#     password = db.Column(db.String(300), nullable=False)

#     def __repr__(self):
#         return f'<User {self.wallet_address}>'

# # 确保在应用启动时创建数据库表
# with app.app_context():
#     db.create_all()  # 创建数据库和表

# # 登录页面
# @app.route('/', methods=['GET', 'POST'])
# def index():
#     if request.method == 'POST':
#         wallet_address = request.form['wallet_address']
#         password = request.form['password']

#         # 查询用户是否存在
#         user = User.query.filter_by(wallet_address=wallet_address).first()
#         if user and check_password_hash(user.password, password):  # 使用check_password_hash验证加密密码
#             # session['wallet_address'] = user.wallet_address
#             return redirect(url_for('main')) # 成功登录后跳转到主页面
#         else:
#             msg = "Invalid username or password! Please check your credentials or register for an account."
#             return render_template('index.html', message=msg)

#     return render_template('index.html')



# @app.route('/register', methods=['GET', 'POST'])
# def register():
#     if request.method == 'POST':
#         wallet_address = request.form['wallet_address']
#         password = request.form['password']

#         # 检查用户是否已存在
#         existing_user = User.query.filter_by(wallet_address=wallet_address).first()
#         if existing_user:
#             msg = "User already exists! Try another username!"
#             return render_template('register.html', message=msg)

#         # 使用 generate_password_hash 对密码进行加密
#         hashed_password = generate_password_hash(password, method='pbkdf2:sha256')

#         # 创建新用户，并将加密后的密码存储到数据库
#         new_user = User(wallet_address=wallet_address, password=hashed_password)
#         db.session.add(new_user)
#         db.session.commit()

#         return redirect(url_for('index'))

#     return render_template('register.html')


# @app.route('/main',methods=["get","post"])
# def main():
#     # r = request.form.get("q")
#     r = request.form.get("wallet_address")
#     # wallet_address = session.get('wallet_address')  # 从 session 中获取用户名
#     current_time = datetime.datetime.now()
#     conn = sqlite3.connect('instance/account.db')
#     c = conn.cursor()
#     c.execute("insert into user values (?, ?)", (r, current_time))
#     conn.commit()
#     c.close()
#     conn.close()
#     return render_template('main.html',r=r)

# @app.route('/store_money',methods=["get","post"])
# def store_money():
#     return render_template('store_money.html')

# @app.route('/transfer_money',methods=["get","post"])
# def transfer_money():
#     return render_template('transfer_money.html')

# @app.route('/admin',methods=["get","post"])
# def admin():
#     return render_template('admin.html')

# @app.route('/viewDB',methods=["get","post"])
# def viewDB():
#     conn = sqlite3.connect('dapp.db')
#     c = conn.cursor()
#     c.execute("select * from user")
#     r = ""
#     for row in c:
#         r += str(row) + "\n"
#     conn.commit()
#     c.close()
#     conn.close()
#     return render_template('viewDB.html',r=r)

# @app.route('/delDB',methods=["get","post"])
# def delDB():
#     conn = sqlite3.connect('dapp.db')
#     c = conn.cursor()
#     c.execute("delete from user")
#     conn.commit()
#     c.close()
#     conn.close()
#     return render_template('deleteDB.html')

# if __name__=='__main__':
#     app.run()


# 初始化Flask应用
app = Flask(__name__)

# 配置SECRET_KEY和数据库URI，指定数据库路径
app.config['SECRET_KEY'] = 'your_secret_key'  # 设置SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///account.db'  # 使用 'sqlite:///account.db' 指定新的数据库

# 初始化数据库
db = SQLAlchemy(app)

# 定义User模型
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    wallet_address = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(300), nullable=False)
    last_time_login = db.Column(db.DateTime, nullable=True)  

    def __repr__(self):
        return f'<User {self.wallet_address}>'
    
class LoginHistory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)  # 外键关联 User 表
    login_time = db.Column(db.DateTime, nullable=False)  # 记录每次登录的时间

    def __repr__(self):
        return f'<LoginHistory {self.user_id} logged in at {self.login_time}>'


# 确保在应用启动时创建数据库表
with app.app_context():
    db.create_all()  # 创建数据库和表

# 登录页面
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        wallet_address = request.form['wallet_address']
        password = request.form['password']

        # 查询用户是否存在
        user = User.query.filter_by(wallet_address=wallet_address).first()
        if user and check_password_hash(user.password, password):  # 使用check_password_hash验证加密密码
            # 存储 wallet_address 到 session
            session['wallet_address'] = user.wallet_address
            # 更新 last_time_login 为当前时间
            user.last_time_login = datetime.datetime.now()
            # 记录登录历史，插入到 LoginHistory 表中
            login_history = LoginHistory(user_id=user.id, login_time=datetime.datetime.now())
            db.session.add(login_history)
            db.session.commit()
            
            return redirect(url_for('main'))  # 成功登录后跳转到主页面
        else:
            msg = "Invalid username or password! Please check your credentials or register for an account."
            return render_template('index.html', message=msg)

    return render_template('index.html')

# 注册页面
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        wallet_address = request.form['wallet_address']
        password = request.form['password']

        # 检查用户是否已存在
        existing_user = User.query.filter_by(wallet_address=wallet_address).first()
        if existing_user:
            msg = "User already exists! Try another username!"
            return render_template('register.html', message=msg)

        # 使用 generate_password_hash 对密码进行加密
        hashed_password = generate_password_hash(password, method='pbkdf2:sha256')

        # 创建新用户，并将加密后的密码存储到数据库
        new_user = User(wallet_address=wallet_address, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('index'))

    return render_template('register.html')

# 主页面
@app.route('/main', methods=["GET", "POST"])
def main():
    # wallet_address = request.form.get("wallet_address")
    # 从 session 中获取 wallet_address
    wallet_address = session.get('wallet_address')
    
    current_time = datetime.datetime.now()

    # # 插入新数据到数据库中 (确保表结构正确)
    # new_record = User(wallet_address=wallet_address, password="dummy_password")  # 假设要插入新用户，密码是虚拟数据
    # db.session.add(new_record)
    # db.session.commit()

    return render_template('main.html', r=wallet_address)

@app.route('/viewDB', methods=["GET", "POST"])
def viewDB():
    users = User.query.all()  # 查询所有用户
    login_histories = LoginHistory.query.order_by(LoginHistory.login_time).all()  # 查询所有登录历史记录
    return render_template('viewDB.html', users=users, login_histories=login_histories)


# 删除数据库内容
@app.route('/delDB', methods=["GET", "POST"])
def delDB():
    User.query.delete()  # 删除所有用户记录
    db.session.commit()
    return render_template('deleteDB.html', message="All records have been deleted.")

# 存储金钱页面
@app.route('/store_money', methods=["GET", "POST"])
def store_money():
    return render_template('store_money.html')

# 转账页面
@app.route('/transfer_money', methods=["GET", "POST"])
def transfer_money():
    return render_template('transfer_money.html')

# 管理员页面
@app.route('/admin', methods=["GET", "POST"])
def admin():
    return render_template('admin.html')

# 启动应用
if __name__ == '__main__':
    app.run(debug=True)
