class Node():
    """ class """

    def __init__(self, name):
        print "initialize"
        self.children = []
        self.name = name

    def add(self, node):
        self.children.append(node)
        node.parent = self

    def set_parent(self, parent):
        self.parent = parent

    def show_all(self):
        for i in self.children:
            print("node name is...")
            i.show()

    def show(self):
        print("name   = {0}.".format(self.name))
        print("parent = {0}.".format(self.parent.name))
