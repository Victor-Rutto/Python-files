class Instructor:
    followers_count = 0  # Class object variable

    def __init__(self, name, address):
        self.name = name
        self.address = address

    def display(self, subject_name):
        # Function becomes a method when it is attached to a particular object
        # We attach using self
        return f'Hello, I am {self.name} and I teach {subject_name}'

    def add_follower(self, follower_name):
        self.followers_count += 1

instructor_1 = Instructor('Victor', 'Nairobi')
instructor_1.display('Python')
instructor_1.add_follower('Monica')
print(instructor_1.display('Python'))
print(instructor_1.followers_count)
instructor_2 = Instructor ('Monica', 'Eldoret')
instructor_2.display('Python')
print(instructor_2.display('Python'))

