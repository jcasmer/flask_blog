from flask import render_template, request, Blueprint
from Flask_blog.models import Post
from flask_login import login_required

main = Blueprint('main', __name__)


@main.route("/")
@main.route("/home")
@login_required
def home():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(per_page=3, page=page)
    return render_template('templates/home.html', posts=posts)


@main.route("/about")
@login_required
def about():
    return render_template('templates/about.html', title='About')
