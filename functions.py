# def get_todos(filepath ='todos.txt'):
#     with open(filepath,'r') as file_local:
#         todos_local = file_local.readlines()
#         return todos_local



# def write_todos(filepath='todos.txt',todos_arg):
#     """ Write a todo items list in the text file. """
#     with open(filepath,'w') as file:
#         file.writelines(todos_arg)


def get_todos(filepath ='todos.txt'):
    with open(filepath,'r') as file_local:
        todos_local = file_local.readlines()
        return todos_local

def write_todos(todos_arg, filepath='todos.txt'):
    """ Write a todo items list in the text file. """
    with open(filepath,'w') as file:
        file.writelines(todos_arg)
