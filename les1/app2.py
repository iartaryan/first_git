print('ЛИСТЫ', '\n', '***'*10)
a = [2,3,4,5,7,6]

print(a)

a.append('Python')

print('First:', a[0], 'Last:', a[-1])

print(a[2:4])

print(len(a))

print(a.index(6))

a.remove('Python')

print(a)

print('СЛОВАРИ', '\n', '***'*10)

user = {'name':'Masha', 'age':25, 'have_airplain':False}

print(user['name'])
print(user.get('name'), user.get('value'))
del user['age']
print(user)