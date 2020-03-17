self={
    "name":"Sekina",
    "age":10
}
# returns a list of tuples of all keys, value pairs
print(self.items())
# returns a list of values in the dict
values=(self.values())
for value in values:
    print(value)
# returns a list of keys in the dict
print(self.keys())