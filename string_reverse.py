class Reverse:
    def __init__(self, s = "s"):
        self.s = s
    def reverse_string(self):
       return self.s[::-1]

word = input("Enter a Word:")

obj = Reverse(word)

print("Reversed String:", obj.reverse_string())



    
