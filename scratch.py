class Post():
    #text = None
    def __init__(self, author, text):
        self.text = text
        self.author = author

    def __repr__(self):
        return self.author + ': ' + self.text


post1 = Post('hoodie alan', 'ill give it to you no interruption')
post2 = Post('jack harlow', 'whats poppin')
post3 = Post('lil wayne', 'same old throne new dragons')

print(post1)