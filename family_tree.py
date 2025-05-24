import enum

class family:
    father=""
    mother=""
    children_name=[]
    
    def __init__(self, user, father, mother, children_name):
        self.user = user
        self.father=father
        self.mother=mother
        self.children_name=children_name

    def children_count(self):
        return len(self.children_name)

class RelateTOHeadofFam(enum):
    my_self = 0,
    Father = 1,
    Mother = 2,
    Spouse = 3,
    Sibling = 4,
    Child = 5


member = family(RelateTOHeadofFam.my_self, "manoharan", "gayathri", ["sanjay", "nisha", "ajay"])


print(member.children_count())
