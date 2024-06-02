class ToDoList:
    tasks = []
    def init(self,):
        self.tasks = []
        self.variants = 0

    def save(self):
        with open('users', 'a') as r:
            r.write(f'{self.variants1}' + '\n')

    #добавление значения
    def add_in_list(self):
        print('Исходный список')
        self.viev_tasks()
        self.variants = input('Поделись чем-нибудь: ')
        self.tasks.append(self.variants)
        print('Измененный список')
        self.viev_tasks()
        self.save()

    #вывод значений
    def viev_tasks(self):
        for i, task in enumerate(self.tasks):
            print(i,'. ', task)

    #Удаление значения
    def remove_list(self):
        while True:
            try:
                print('Исходный список')
                self.viev_tasks()
                self.variants = input('Какую по номеру задачу вы хотите удалить нафиг?')
                self.tasks.remove(self.tasks.index(self.variants))
                print('Измененный список')
                self.viev_tasks()
                self.save()
                break
            except:
                print('Попробуйте снова')


    def choose_action(self):
        match input('Выберите действие:\n1 - Добавить в список\n2 - Посмотеть список\n3 - Удалить из списка\n4 - ВЫХОД\n'):
            case '1':
                 self.add_in_list()
            case '2':
                 print('Исходный список')
                 self.viev_tasks()
            case '3':
                 self.remove_list()
            case '4':
                quit()
            case _:
                print('Смешной')




def main():
    somelist = ToDoList()

    while True:
        somelist.choose_action()



if __name__ == '__main__':
    main()


























