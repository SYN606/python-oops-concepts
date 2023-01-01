class Dad:
    basketball = 1

class Son(Dad):

    dance = 1
    def is_dance(self):
        return f"Yes, I dance {self.dance} no of times"

class GrandSon(Son):
    guitar = 1
    dance = 6
    def is_dance(self):
        return f"I am grandson and i dance {self.dance} no. of times."


ayush = Dad()
ram = Son()
shyam = GrandSon()

# print(shyam.basketball)
print(shyam.is_dance())