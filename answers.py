def get_answer(key):
	answer = {'привет':'И тебе привет','Как дела?':'Лучше всех!', 'Пока':'Увидимся'}
	return answer.get(key, 'Не знаю о чем ты')

print(get_answer(input('Введите что-нибудь: ').lower()))