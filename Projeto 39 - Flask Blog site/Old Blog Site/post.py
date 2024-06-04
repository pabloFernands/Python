import requests


class Post:

    def __init__(self):
        blog_list = []
        self.blog_adress = "https://api.npoint.io/c790b4d5cab58020d391"
        blog_response = requests.get(self.blog_adress)
        blog = blog_response.json()
        for new_blog in blog:
            blog_entry = {
                "title": new_blog["title"],
                "subtitle": new_blog["subtitle"],
                "body": new_blog["body"]
            }
            blog_list.append(blog_entry)
        return blog_list
        #print(self.blog_title)

