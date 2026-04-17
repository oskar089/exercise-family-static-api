"""
Update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint


class FamilyStructure:
    id = 0
    def __init__(self, last_name):
        self.last_name = last_name

        # example list of members
        self._members = []

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):

        self.id+=1
        return self.id

    def add_member(self, member):
        # fill this method and update the return
        if "id" not in member:
            member["id"] = self._generateId()

        # Siempre nos aseguramos de que el apellido sea el de la familia
        member["last_name"] = self.last_name
        print(member) 
        self._members.append(member)

    def delete_member(self, id):
        # fill this method and update the return
        # Filtramos la lista para quitar al miembro con ese id
        for i in range(len(self._members)):
            if self._members[i]["id"] ==id:
                self._members.pop(i)
                return True
        return False

    def get_member(self, id):
        # fill this method and update the return
        # Buscamos al miembro por id
        for member in self._members:
            if member["id"] == id:
                return member
        return None


    # This method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members
    
