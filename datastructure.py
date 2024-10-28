from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        self._members = [] 

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        # fill this method and update the return
        self._members.append(member)
        pass

    def delete_member(self, id):
        # fill this method and update the return
        pass

    def get_member(self, member_id):
        for member in self._members:  
            if member['id'] == member_id:
                return member
        return None 

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members