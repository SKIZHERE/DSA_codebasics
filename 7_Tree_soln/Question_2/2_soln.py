class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def print_tree(self, level):
        if self.get_level() <= level:
            space = "   "*self.get_level()+"|__" if self.parent else ""
            print(space + self.data)
            if self.children:
                for child in self.children:
                    child.print_tree(level)

def build_product_tree():
    Global = TreeNode("Global")

    india = TreeNode("India")
    guj = TreeNode("Gujrat")
    guj.add_child(TreeNode("Ahmedabad"))
    guj.add_child(TreeNode("Baroda"))
    kar = TreeNode("Karnataka")
    kar.add_child(TreeNode("Bangluru"))
    kar.add_child(TreeNode("Mysore"))
    india.add_child(guj)
    india.add_child(kar)

    usa = TreeNode("USA")
    newj = TreeNode("New Jersey")
    newj.add_child(TreeNode("Princeton"))
    newj.add_child(TreeNode("Trenton"))
    cali = TreeNode("California")
    cali.add_child(TreeNode("San Francisco"))
    cali.add_child(TreeNode("Mountain View"))
    cali.add_child(TreeNode("Palo Alto"))
    usa.add_child(newj)
    usa.add_child(cali)

    Global.add_child(india)
    Global.add_child(usa)

    return Global

if __name__ == '__main__':

    root = build_product_tree()
    root.print_tree(1)
    root.print_tree(2)
    root.print_tree(3)