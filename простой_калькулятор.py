def calculate(x:float, y:float, operation:str='a') -> None:
    """Простой калькулятор

    Args:
        x (float): _description_
        y (float): _description_
        operation (str, optional): _description_. Defaults to 'a'.
    """
           
    def addition():
        print(x+y)

    def subtraction():
        print(x-y)

    def division():
        if x == 0 or y == 0:
            print("На ноль делить нельзя!")
        else:
            print(x/y)

    def multiplication():
        print(x*y)

    operation_dict = {'a': addition,
                    's': subtraction,
                    'd': division,
                    'm': multiplication
                      }
    if operation_dict.get(operation) is None:
        print("Ошибка. Данной операции не существует")
    else:
        operation_dict[operation]()
                       
calculate(0, 10, "d")      
    