def test():

	user_info = {}

	user_info['first_name'] = input('Введите свое имя: ')
	user_info['last_name'] = input('Введите свою фамилию: ')

	print(user_info)



def get_summ(one, two, delimeter = ' '):
	all_test = str(one) + str(delimeter) + str(two)
	return all_test.upper()

print(get_summ('hello', 2))