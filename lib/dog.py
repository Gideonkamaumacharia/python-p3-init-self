class Dog:
    def __init__(self,name,breed = "Mutt"):
       self.breed = breed
       self.name = name
    def bark(self):
       print(f"{self.name} is a {self.breed} breed")
       print(f"{self.name} is barely 3 days and he can bark!")

    def adopted(self,owner):
       if not isinstance(owner,str):
            return "Invalid data type"
       else:
           self.owner = owner
           return owner
fido = Dog("Fido")
fido.bark()

snoopy = Dog("Snoopy","Chiwawa")
snoopy.bark()

#snoopy.owner = "Gideon"
#print(f"{snoopy.owner} is the owner of {snoopy.name}")

fido.adopted("Sophie")
print(fido.owner)