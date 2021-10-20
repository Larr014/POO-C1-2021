class Persona:

    def __init__(self,fullname,profession,birth,genre,bodyweight,height,nationality,id=''):
        self.__fullname = fullname
        self.__profession = profession
        self.__birth = birth
        self.__genre = genre
        self.__bodyweight = bodyweight
        self.__height = height
        self.__nationality = nationality
        self.__id = id

    #Cuando un atributo es privado la unica opcion de obtener dicho atributo desde otra parte es con un get
    def get_fullname(self):
        return self.__fullname

    def get_profession(self):
        return self.__profession

    def get_birth(self):
        return self.__birth

    def get_genre(self):
        return self.__genre

    def get_bodyweight(self):
        return self.__bodyweight

    def get_height(self):
        return self.__height

    def get_nationality(self):
        return self.__nationality

    def set_fullname(self,fullname):
        self.__fullname = fullname