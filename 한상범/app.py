from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!!!!'

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username

@app.route('/hello/<name>')
def hello(name=None):
    # 1) 템플릿의 이름, 2) 템플릿에 보여줄 변수
    return render_template('hello.html', name=name)

if __name__ == '__main__':
    app.run(debug = True)