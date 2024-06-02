# решил воспользоваться алгоритмом "Быстрый поиск" со сложностью O(nlogn) о котором я узнал в книге "Грокаем Алгоритмы"

def qsort(array):
    if len(array) < 2:
        return array     #если в массиве находиться менее двух элементов, то он уже считается отсортированным
    else:
        element = array[0] # берем опорную точку

        less = [i for i in array[1:] if i < element] #если элементы меньше опорной точки, то мы откладываем их в массив less

        greater = [i for i in array[1:] if i > element] # Если элементы больше опорной точки, то мы откладываем их в массив greater

        return  qsort(less) + [element] + qsort(greater) # Соединяем
