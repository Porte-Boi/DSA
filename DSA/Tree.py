# class Treenode:
#     def  __init__(self,data):
#         self.data = data
#         self.children = []
#         self.parent = None

#     def add_child(self,child):
#         self.child = child
#         child.parent = self
#         self.children.append(child)
    
#     def get_level(self):
#         level = 0
#         p = self.parent
#         while p:
#             level += 1
#             p = p.parent

#         return level

#     def print_tree(self):
#         spaces = " " * self.get_level() * 2
#         prefix = spaces + "|__" if self.parent else ""
#         print(prefix + self.data)
#         if self.children:
#             for child in self.children:
#                 child.print_tree()




# def build_prodrct_tree():
#     root = Treenode("Electronics")

#     laptop = Treenode("Laptop")
#     laptop.add_child(Treenode("Mac"))
#     laptop.add_child(Treenode("Surface"))
#     laptop.add_child(Treenode("Thinkpad"))

#     cellphone = Treenode("Cell Phone")
#     cellphone.add_child(Treenode("iphone"))
#     cellphone.add_child(Treenode("Pixal"))
#     cellphone.add_child(Treenode("Vivo"))

#     tv = Treenode("Tv")
#     tv.add_child(Treenode("Samsung"))
#     tv.add_child(Treenode("LG"))
    
#     root.add_child(laptop)
#     root.add_child(cellphone)
#     root.add_child(tv)

#     return root

# if __name__ == '__main__':
#     root = build_prodrct_tree()
#     root.print_tree()

#     pass

# class Treenode:
#     def __init__(self, name, designation):
#         self.name = name
#         self.designation = designation
#         self.children = []
#         self.parent = None
    
#     def get_level(self):
#         level = 0
#         p = self.parent
#         while p:
#             level += 1
#             p = p.parent
#         return level
    
#     def print_tree(self, property_name):
#         if property_name == "both":
#             value = self.name + " (" + self.designation + ") "
#         elif property_name == "name":
#             value = self.name
#         else:
#             value = self.designation

#         spaces = " " * self.get_level() * 2
#         prefix = spaces + "|--" if self.parent else ""
#         print(prefix + value)
#         if self.children:
#             for child in self.children:
#                 child.print_tree(property_name)
    
#     def add_child(self, child):
#         self.child = child
#         child.parent = self
#         self.children.append(child)

# def build_management_tree():
#     # Infra Deparment
#     infra_head = Treenode("vishwa", "Infrustructure Head")
#     infra_head.add_child(Treenode("Dhaval", "Cloud Manager"))
#     infra_head.add_child(Treenode("Abhijit", "App Maneger"))

#     # Cto deparment
#     cto = Treenode("Chinmay", "CTO")
#     cto.add_child(infra_head)
#     cto.add_child(Treenode("Amir", "Application Manager"))

#     # Hr Department
#     hr_head = Treenode("Gels", "HR Head")
#     hr_head.add_child(Treenode("Peter", "Recruitment Manager"))
#     hr_head.add_child(Treenode("Waqas", "Policy Manager"))

#     # CEO , all deparment work under him
#     ceo = Treenode("Nilpul", "CEO")
#     ceo.add_child(cto)
#     ceo.add_child(hr_head)

#     return ceo

# if __name__ == "__main__":
#     root = build_management_tree()
#     root.print_tree("both")


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level
    
    def print_tree(self, level):
        
        
        spaces = " " * self.get_level() * 4
        prefix = spaces + "|--" if self.parent else ""
        print(prefix + self.data)

        if self.children:
            for child in self.children:
                child.print_tree(level)
        
    def add_child(self, child):
        child.parent = self
        self.children.append(child)

def build_location_tree():
    root = TreeNode("Global")

    bd = TreeNode("Bangladesh")

    dhaka = TreeNode("Dhaka")
    dhaka.add_child(TreeNode("Mirpur"))
    dhaka.add_child(TreeNode("Gulshan"))

    ctg = TreeNode("Chittagong")
    ctg.add_child(TreeNode("Nasirabad"))
    ctg.add_child(TreeNode("Cox's Bazar"))

    bd.add_child(ctg)
    bd.add_child(dhaka)

    usa = TreeNode("USA")

    nj = TreeNode("New Jersey")
    nj.add_child(TreeNode("Princton"))
    nj.add_child(TreeNode("Trenton"))

    cf = TreeNode("Califonia")
    cf.add_child(TreeNode("San Francisco"))
    cf.add_child(TreeNode("Mountain View"))
    cf.add_child(TreeNode("Palo Alto"))

    usa.add_child(nj)
    usa.add_child(cf)

    root.add_child(bd)
    root.add_child(usa)

    return root

if __name__ == "__main__":
    root_node = build_location_tree()
    root_node.print_tree(3)