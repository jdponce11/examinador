class Book():
    # Constructor method for book objects
    def __init__(self, name, author, pathtofile):
        self.name = name
        self.author = author
        self._pathtofile = None
        self.pathtofile = pathtofile
        self.text = None

    @property
    def pathtofile(self):
        return self._pathtofile

    @pathtofile.setter
    def pathtofile(self, new_path):
        self.text = None
        self._pathtofile = new_path

