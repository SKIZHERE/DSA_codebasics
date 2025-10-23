class TreeNode:
    def __init__(self, designation, name):
        self.name = name
        self.designation = designation
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

    def print_tree(self, type):
        space = "   "*self.get_level()+"|__" if self.parent else ""
        if type == "name":
            print(space + self.name)
        elif type == "designation":
            print(space + self.designation)
        elif type == "both":
            print(space + self.name + " (" + self.designation + ")")
        if self.children:
            for child in self.children:
                child.print_tree(type)

def build_product_tree():
    ceo = TreeNode("CEO", "Nilupul")

    cto = TreeNode("CTO", "Chinmay")
    ih = TreeNode("Infrastructure head", "Vishwa")
    ih.add_child(TreeNode("Cloud manager","Dhaval"))
    ih.add_child(TreeNode("App manager", "Abhijit"))
    cto.add_child(ih)
    cto.add_child(TreeNode("Application head", "Aamir"))

    hrhead = TreeNode("HR head","Gels")
    hrhead.add_child(TreeNode("Recruitment manager", "Peter"))
    hrhead.add_child(TreeNode("Policy manager", "Waqas"))

    ceo.add_child(cto)
    ceo.add_child(hrhead)

    return ceo

if __name__ == '__main__':

    root = build_product_tree()
    root.print_tree("name")
    root.print_tree("designation")
    root.print_tree("both")
    pass