from flask import render_template, request, Blueprint
from webapp.models import Post

main = Blueprint('main', __name__)

@main.route("/")
@main.route("/home")
def home():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template('home.html', posts=posts)

@main.route("/pachome")
def pachome():
    page = request.args.get('page', 1, type=int)
    #posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    #flash(f'Current User: {str(current_user)}')
    #return render_template('pachome.html', posts=posts)
    return render_template('pachome.html')

@main.route("/about")
def about():
    return render_template('about.html', title='About')
