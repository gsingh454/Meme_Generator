# encapsulating the quotes fetched from files.
class QuoteModel(object):
    # encapsulating body and author
    def __init__(self, body, author):
        # initialization of body and author by getting it.
        self.body = body
        self.author = author

    def __repr__(self):
        return f'{self.body} -- {self.author}'
