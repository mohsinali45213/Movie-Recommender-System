from os import path
print(__file__)
# i wanna go back
parents = path.dirname(path.abspath(__file__))
print(parents)
grandparents = path.dirname(parents)
print(grandparents)