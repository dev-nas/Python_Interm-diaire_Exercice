from datetime import datetime

class Person:
    _id = 0
    first_name = ""
    last_name = ""
    
    def __init__(self, _id, f, l):
        if not isinstance(f, str):
            raise TypeError("firstname must be a string !")
        self._id = _id
        self.first_name = f
        self.last_name = l
    
    def getFullName(self):
        return "{} {}".format(self.first_name.capitalize(), self.last_name.upper())

class Client(Person):
    _id = 0
    _date_joint = None
    _date_format = "%Y/%m/%d"
    #le constructeur doit tenir compte des attributs hérités de Person
    def __init__(self, _id, dj, _idp, f, l):
        #appel au constructeur de la classe mère
        super().__init__(_idp, f, l)
        #initialisation des attibuts propres
        self._id = _id
        self._date_joint = datetime.strptime(dj, self._date_format)
    
    def getDateJoint(self, _format=""):
        if not _format:
            return self._date_joint
        return self._date_joint.strftime(_format)