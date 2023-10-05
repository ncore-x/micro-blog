from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [
    {
        'author': 'Ivan Ivanov',
        'title': 'Blog posts 1',
        'content': 'First post content',
        'date_posted': 'October 5, 2023',
    },
    {
        'author': 'Petr Petrov',
        'title': 'Blog posts 2',
        'content': 'Second post content',
        'date_posted': 'September 10, 2023',
    },
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


if __name__ == '__main__':
    app.run(debug=True)
