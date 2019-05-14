# coding : utf-8
# PEP-8
# Python-1-lesson3-easy Task 2


"функция определения максимального числа"
def max_input (inlist):
    return(max(inlist, key=lambda x: float(x)))


#"функция ввода пользовательских данных: исключает буквенные символы - этого хватило"
def digit_input ():
    input_list=['a','b','c']
    for id in range(len(input_list)):
        temp_sym = input_list[id]
        while temp_sym.isalpha() or len(temp_sym) <= 0 or temp_sym.isalpha() or temp_sym.isspace():
            temp_sym = input('Введите ваше число {}: '.format(id+1))
        input_list[id] = temp_sym
    return(input_list)

print('\t Максимальное из введённых:', max_input(digit_input()))

# Постарайтесь использовать то, что мы прошли на уроке при решении этого ДЗ,
# вспомните про zip(), map(), lambda, посмотрите где лучше с ними, а где они излишни!

# Задание - 2
# Создайте функцию, принимающую на вход 3 числа, и возвращающую наибольшее из них
