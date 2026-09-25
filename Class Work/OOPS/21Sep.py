class Student:
    def __init__(self,roll,name,sal):
        self.__roll = roll
        self.__name = name
        self.__sal = sal

    @property
    def roll(self):
        return self.__roll

    @property
    def name(self):
        return self.__name

    @property
    def sal(self):
        return self.__sal

    @name.setter
    def name(self,name):
        self.__name = name

    @sal.setter
    def sal(self,sal):
        self.__sal = sal

    @roll.deleter
    def roll(self):
        raise AttributeError("Roll no. can not be deleted")
    
    @name.deleter
    def name(self):
        print("Name Deleted")
        del self.__name

    @sal.deleter
    def sal(self):
        print("Salary Deleted")
        del self.__sal

st = Student(121,"Nayan",60000)
print(st.roll)
print(st.name)
print(st.sal)
st.name = "Yash"
st.sal = 30000
print(st.roll)
print(st.name)
print(st.sal)
del st.name
del st.sal
del st.roll