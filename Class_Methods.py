class Instructor:
    followers= 0  #Class object variable
    def __init__ (self, name, address, ):
        self.name = name
        self.address = address
    def display (self, subject_name): 
        #Fuction becomes a method when it is attached to a particular object
        #We attach using self 
        return(f'Hello I am {self.name} and I teach {subject_name}')
    def add_followers(self, follower_name):
        self.followers += 1

instructor_1 = Instructor ('Victor', 'Nairobi')
instructor_1.display('Python')
instructor_1.add_followers("Monn")
print(instructor_1.display('Python')) 
print(instructor_1.followers)

#print(instructor_1.display('Python'))
#print(instructor_1.address)
instructor_2 =Instructor ('Monica', 'Eldoret')
#Self binds the attribute to the object
print(instructor_2.followers)
