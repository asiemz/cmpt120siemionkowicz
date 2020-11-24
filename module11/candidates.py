#candidates.py



class Attendee:

    def __init__(self,firstname,lastname,company,state):

        self.firstname = firstname
        self.lastname = lastname
        self.company = company
        self.state = state
        self.email = firstname + "." + lastname + "@" + company + ".org"

    def get_name(self):
        return self.firstname + "" + self.lastname

    def get_company(self):
        return self.company

    def get_state(self):
        return self.state

    def get_email(self):
        return self.email


person1 = Attendee("John","Smith","AMD","NJ")
person2 = Attendee("Stuart","Johnson","Google","NY")
person3 = Attendee("Samuel","Long","IBM","NY")

object_list = [person1, person2, person3]












