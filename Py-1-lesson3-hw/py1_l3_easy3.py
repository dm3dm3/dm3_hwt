# coding : utf-8
# PEP-8
# Python-1-lesson3-easy Task 3

"функция определения максимальной длины строки"
def max_inputstr (string):
    return(max(string, key=len))


#"функция ввода пользовательских данных: исключает пустые и короткие символьные строки"
def str_input ():
    input_list=[]
    while True:
        temp_str = ''
        while temp_str.isspace() or (not temp_str.isalnum() and len(temp_str) <= 2) or len(temp_str) == 0:
            temp_str = input('Введите вашу непустую строку, для окончания ввода наберите "кон": ')
        if temp_str == 'кон':
            break
        else:
            input_list.append(temp_str)
    #print(input_list)
    return(input_list)

print('\n\t Максимальная строка из введённых непустых строк: ', max_inputstr(str_input()))

# Постарайтесь использовать то, что мы прошли на уроке при решении этого ДЗ,
# вспомните про zip(), map(), lambda, посмотрите где лучше с ними, а где они излишни!

# Задание - 3
# Создайте функцию, принимающую неограниченное количество строковых аргументов,
# верните самую длинную строку из полученных аргументов
