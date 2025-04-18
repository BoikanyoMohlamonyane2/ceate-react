id = int(input("Enter your ID: "))
name = input("Enter your name: ")
age = int(input("Enter your age: "))

class Student:  
    def __init__(self, id, name, age):
        self.id = id
        self.name = name
        self.age = age

    def display(self):
        print(f"ID: {self.id}, Name: {self.name}, Age: {self.age}")

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, Age: {self.age}"

    def __repr__(self):
        return f"Student({self.id}, {self.name}, {self.age})"

    def __eq__(self, other):
        if isinstance(other, Student):
            return self.id == other.id and self.name == other.name and self.age == other.age
        return False

    def __lt__(self, other):
        if isinstance(other, Student):
            return self.age < other.age
        return False

    def __le__(self, other):
        if isinstance(other, Student):
            return self.age <= other.age
        return False

    def __gt__(self, other):
        if isinstance(other, Student):
            return self.age > other.age
        return False

    def __ge__(self, other):
        if isinstance(other, Student):
            return self.age >= other.age
        return False

    def __ne__(self, other):
        if isinstance(other, Student):
            return self.id != other.id or self.name != other.name or self.age != other.age
        return False

    def __hash__(self): 
        return hash((self.id, self.name, self.age))

    def __len__(self):              
        return len(self.name)

    def __getitem__(self, index):   
        return self.name[index]

    def __setitem__(self, index, value):
        name_list = list(self.name)
        name_list[index] = value
        self.name = ''.join(name_list)

    def __delitem__(self, index):
        name_list = list(self.name)
        del name_list[index]
        self.name = ''.join(name_list)

    def __contains__(self, item):   
        return item in self.name

    def __iter__(self):
        return iter(self.name)

# Create an instance and print things
s1 = Student(id, name, age)

print(s1)        # Calls __str__
s1.display()     # Calls display method
print(f"Length of name: {len(s1)}")  # __len__

# Indexing
print(f"First letter in name: {s1[0]}")  # __getitem__

# Check containment
print("'a' in name?", 'a' in s1)  # __contains__

# Iteration
print("Letters in name:")
for letter in s1:
    print(letter)
