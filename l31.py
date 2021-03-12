#dictionary - słownik: key:value, nawiasy {}, klucz unikalny, wartość nieunikalna,
rooms = {1: 'kitchen', 7: 'dining room', 2: 'bathroom'}

print(rooms)
print(rooms[1])
print(rooms[7])

#nadpisanie pokoju na kluczu 7
rooms[7] = 'sleeping room'

print(rooms)

#dodanie nowego pokoju
rooms[777] = 'new room'
print(rooms)

#update
rooms.update({700: 'new room2'})
print(rooms)

#del
del(rooms[700])
print(rooms)

#pop
rooms.pop(1)
print(rooms)

#pop item - usuwa ost
rooms.popitem()
print(rooms)

#key może być stringiem
names = {'name': 'Marcin', 'surname': 'King'}
print(names['name'])
print(names['surname'])
print(names.get('surname'))

#len
print(len(names))

#clear
names.clear()
print(names)
