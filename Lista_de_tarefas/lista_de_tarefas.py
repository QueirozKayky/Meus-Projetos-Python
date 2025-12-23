import os 

tasks = []
while True:
        if os.name =='nt':
            os.system('cls')
        else:
            os.system('Clear')

        print('----------------')
        print('   Tasks list   ')
        print('----------------')
        print('[1] Add Task')
        print('[2] See tasks')
        print('[3] Delete task')
        print('[4] Exit System')
        print('----------------')

        decision = int(input('choose one option: '))

        if decision == 1:
            print('You choose option [1]')
            decision1 = str(input('What is your task: '))
            tasks.append(decision1)
            print('Task add with succes.')
            input('Press Enter to continue...')

        elif decision == 2:
            print('You choose option [2]')
            print('this is yours taks, today.')
            for position, task in enumerate(tasks):
                print(f'{position+1} {task}')
            input('Press Enter to continue....')

        elif decision == 3:
            print('You choose option [3]')
            if len(tasks) == 0:
                print('Nothing to delete here.')
                input('Press Enter to continue...')
            else:
                for position, task in enumerate(tasks):
                    print(f'{position+1}. {task}')
                try:
                    task_to_delete = int(input('Type the number of the task that you want delete: '))
                    if 0 < task_to_delete <= len(tasks):
                        removed_task = tasks.pop(task_to_delete - 1)
                        print(f'Task "{removed_task}" removed succesfuly!')
                    else:
                        print('Invalid Number. Please, type a number of list.')
                except ValueError:
                    print('Ops, Invalid Number. Please, type a number of list.')

                input('Type Enter to continue...')


        elif decision == 4:
            print('Bye Bye, see you soon!')
            break