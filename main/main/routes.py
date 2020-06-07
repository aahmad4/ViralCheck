from flask import Blueprint, render_template, request
from main.models import Post
import predict

main = Blueprint('main', __name__)

thumbnails = [
  {
    'author': 'Ali',
    'title': 'Computer Scripting',
    'content': 'Computer Scripting',
    'date_posted': 'June 4 2020',
    'image': 'https://images.unsplash.com/photo-1559526324-4b87b5e36e44?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=500&q=60'
  },
  {
    'author': 'Joey',
    'title': 'Cooling On The Beach',
    'content': 'Second post',
    'date_posted': 'June 4 2020',
    'image': 'https://images.unsplash.com/photo-1541739900389-5f066a7d8c99?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=500&q=600'
  },
  {
    'author': 'Vinchhi',
    'title': 'Having A Fun Adventure',
    'content': 'Second post',
    'date_posted': 'June 4 2020',
    'image': 'https://images.unsplash.com/photo-1550424616-3d37bc3e9a2a?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=500&q=60'
  },
  {
    'author': 'Vinchhi',
    'title': 'Getting Ready For Spring',
    'content': 'Second post',
    'date_posted': 'June 4 2020',
    'image': 'https://images.unsplash.com/photo-1567226055219-bd1ee70f3d5c?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=500&q=60'
  },
  {
    'author': 'Ali',
    'title': 'Testing Out The New Whip',
    'content': 'Second post',
    'date_posted': 'June 4 2020',
    'image': 'https://images.unsplash.com/photo-1566790050901-772dc40a79f3?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=500&q=60'
  },
  {
    'author': 'Billy',
    'title': 'Having Fun In Nature',
    'content': 'Second post',
    'date_posted': 'June 4 2020',
    'image': 'https://images.unsplash.com/photo-1567127214373-7ca7b33baf25?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=500&q=60'
  }
]








@main.route('/', methods=['GET', 'POST'])
def home():
  if request.method == 'POST':
    youtube_url = str(predict.predict(request.form['url']))

    return render_template("index.html", youtube_url=youtube_url)
  
  else:
    return render_template("index.html")

@main.route('/advice')
def advice():
  return render_template("advice.html")

@main.route('/posts')
def images():
  page = request.args.get('page', 1, type=int)
  posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=10)
  return render_template("instagram.html", posts=posts)

@main.route('/gallery')
def gallery():
  return render_template("gallery.html", thumbnails=thumbnails)
