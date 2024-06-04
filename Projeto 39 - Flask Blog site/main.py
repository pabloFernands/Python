from flask import Flask, render_template, request
import requests

app = Flask(__name__)

def get_blog():
    blog_adress = "https://api.npoint.io/674f5423f73deab1e9a7"
    blog_response = requests.get(blog_adress)
    blog = blog_response.json()
    blog_list = []
    for new_blog in blog:
        blog_entry = {
            "id": new_blog["id"],
            "title": new_blog["title"],
            "subtitle": new_blog["subtitle"],
            "body": new_blog["body"]
        }
        blog_list.append(blog_entry)
    return blog_list

@app.route('/')
def get_all_posts():
    info_blog = get_blog()
    first_title = info_blog[0]["title"]
    first_subtitle = info_blog[0]["subtitle"]
    first_id = 0
    second_title = info_blog[1]["title"]
    second_subtitle = info_blog[1]["subtitle"]
    second_id = 1
    third_title = info_blog[2]["title"]
    third_subtitle = info_blog[2]["subtitle"]
    third_id = 2
    return render_template("index.html", first_title=first_title, first_subtitle=first_subtitle,
                           first_id=first_id, second_title=second_title, second_subtitle=second_subtitle, second_id=second_id,
                           third_title=third_title, third_subtitle=third_subtitle, third_id=third_id)


@app.route('/post/<blog_id>')
def blog(blog_id):
    blog_integer = int(blog_id)
    info_blog = get_blog()
    find_blog = info_blog[blog_integer]
    return render_template("post.html", title=find_blog["title"], subtitle=find_blog["subtitle"],
                           body=find_blog["body"])


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/form-entry", methods=["POST"])
def receive_data():
    data = request.form
    print(data["name"], data["email"], data["phone"])
    return "<h1>Successfully sent your message</h1>"

# @app.route("/post")
# def post():
#     return render_template("post.html")


if __name__ == "__main__":
    app.run(debug=True)

