# 3. You realize that you need to add 'black panther' after 'hulk',
#    so remove it from the list first and then add it after 'hulk'

heros=['spider man', 'thor', 'hulk', 'iron man', 'captain america', 'black panther']
print(heros)

heros.remove('black panther')
print(heros)

heros.insert(3,'black panther')
print(heros)
