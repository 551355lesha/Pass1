
# простая реализация с использованием списка, поэтому простая читаемость кода.
# если удалить элемент в начале списка, прийдеться сдвигать все вперед.


class FirstInFirstOut:


    def __init__(self, element):
        self.element = element
        self.queue = []



    def add(self, item):
        if len(self.queue) < self.element:
            self.queue.append(item)
        else:
            self.queue.pop(0)
            self.queue.append(item)




    def get(self):
        return self.queue








