#
#  This file is for defining 'classes' within the context of the website
#
#####################################################################


class ChatRoom():
    var = 'test'


class User():
    var = 'test'


class Post():
    def __init__(self, author, text):
        self.author = author
        self.text = text

    def __repr__(self):
        return self.author + ': ' + self.text


post1 = Post('hoodie alan', 'ill give it to you no interruption')
post2 = Post('jack harlow', 'whats poppin')
post3 = Post('lil wayne', 'same old throne new dragons')

test_posts = [post1, post2, post3]
