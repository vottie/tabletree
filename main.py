from node import Node
from leaf import Leaf

if __name__ == '__main__':
    """ prepare """ 
    print("start")
    parent = Node("root")
    leaf1 = Leaf("1-1")
    parent.add(leaf1)
    leaf2 = Leaf("1-2")
    parent.add(leaf2)
    node2 = Node("node2")
    parent.add(node2)

    """ execute """ 
    parent.show_all()
