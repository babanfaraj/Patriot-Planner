from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route('/')
@app.route('/index.html')
def index():
    return render_template("index.html")


@app.route('/about.html')
def about():
    return render_template("about.html")


@app.route('/blog.html')
def blog():
    return render_template("blog.html")


@app.route('/blog-details.html')
def blog_details():
    return render_template("blog-details.html")


@app.route('/contact.html')
def contact():
    return render_template("contact.html")


@app.route('/event-gallery.html')
def event_gallery():
    return render_template("event-gallery.html")


@app.route('/event-schedule.html')
def event_schedule():
    return render_template("event-schedule.html")


@app.route('/price.html')
def price():
    return render_template("price.html")


@app.route('/speaker.html')
def speaker():
    return render_template("speaker.html")


if __name__ == '__main__':
    app.run(debug=True)  #host='0.0.0.0', port=80)
