# coding : utf-8
# PEP-8
# Python-1-lesson1-hard Task 1

vera = 10 ** 4
verb = 10.1
verc = False
print('\tMedical form, please fill it out:\n')
name = input ('\tYour name: ')
surname = input('\tYour surname: ')
age = input('\t\tYour age: ')
wght = input('\tYour weight, kg: ')

if len(name) > 0 and len(surname) > 0 and len(age) > 0 and len(wght) > 0 and wght.isdigit() and\
        age.isdigit() and name.isalpha() and surname.isalpha():
    vuser_params = {'name': name, 'surname': surname,  'age': age, 'weight': wght}
    # лишняя конечно операция - но так ради обкатки материала
    print('\nThe patient: ', vuser_params['name'], vuser_params['surname'], '\n\t who ',
          vuser_params['age'], ' years old and weight ', vuser_params['weight'], ' kg. \nDiagnosis: \n\t')
    if 14 <=  int(age) <= 30 and 120 >= int(wght) >= 50:
        print('Good helth!')
    elif 40 >= int(age) > 30  and not (120 >= int(wght) >= 50):
        print('Pls add some phisical education for youself.')
    elif 80 > int(age) > 40 and not (120 >= int(wght) >= 50):
        print('Pls consult a doctor.')
    elif 80 <= int(age):
        print('Don\'t worry, please/')
    elif int(age) < 14:
        print('Pls consult a with child doctor.')
    else:
        print('Need additional research.')
else:
    print('Your input incorrect. Sorry, dear, patient!\n')
