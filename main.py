from node import Node
from leaf import Leaf

if __name__ == '__main__':
    """ prepare """ 
    print("start")
    root = Node("root")
    leaf1 = Leaf("1-1")
    leaf1.set_parent(root)
    leaf2 = Leaf("1-2")
    leaf2.set_parent(root)
    node2 = Node("node2")
    node2.set_parent(root)
    node3 = Node("node3")
    node3.set_parent(node2)

    root.add(leaf1)
    root.add(leaf2)
    root.add(node2)

    node2.add(node3)

    """ execute """ 
    root.show_all()
    node2.show_all()
