
class Actor:
    def __init__(self,fullname):
        if fullname!="" and type(fullname) is str:
            self.name=fullname.strip()
        else:
            self.name=None
        self.colleagues=[]

    @property
    def actor_full_name(self):
        return self.name

    def __repr__(self):
        return f"<Actor {self.name}>"

    def __eq__(self, other):
        if type(other) is Actor:
            return self.actor_full_name == other.actor_full_name
        return False

    def __lt__(self, other):
        return self.actor_full_name < other.actor_full_name

    def __hash__(self):
        return hash(self.actor_full_name)

    def add_actor_colleague(self,colleague):
        if type(colleague) is Actor:
            self.colleagues.append(colleague)

    def check_if_this_actor_worked_with(self,colleague):
        if type(colleague) is Actor:
            return colleague in self.colleagues
        return False
