
weather = {'city':'Москва', 'temperature':20, 'wind':'Восточный'}
weather_1 = {'city':'Нью-Йорк', 'temperature':25, 'wind':'Западный','date':'2.01.2017'}
weather_2 = {'city':'Лондон', 'temperature':27, 'wind':'Северный', 'date':'13.03.1990'}

print(weather['city'])

weather['temperature'] = 10

print(weather['temperature'])

print(len(weather))

print(weather.get('country'))

weather['date'] = '27.05.2017'

#print(weather)



weather_list = [weather]
weather_list.append(weather_1)
weather_list.append(weather_2)

print('Лист:')
for i in weather_list:
	print(i)
#	print(i['city'],i['temperature'],i['wind'],i['date'])
