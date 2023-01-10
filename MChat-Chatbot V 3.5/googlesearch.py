from googlesearch import search

query = input("ENter Query: ")

print(search(query, tld='com', num=2, stop =2))

