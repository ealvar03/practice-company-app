from company_employee.company import Company
from company_employee.contextual_menu import ContextualMenu

if __name__ == '__main__':
    # *********************************
    #           Dummy data
    # *********************************
    # my_company = Company()
    #
    # my_company.create_employee('Elena', '32', '123456', 'single', 'IT', '2000', 'manager', 'John Williams', '16',
    #                            '890', 'London')
    # my_company.create_employee('Ines', '28', '111111', 'married', 'IT', '1500', 'admin', 'Bermondsey', '2',
    #                            '222', 'Romford')
    # my_company.create_department('HR', '1234', 'London', 'Axa')
    # my_company.create_department('IT', '1111', 'London', 'Axa')
    # my_company.create_department('Reception', '14355', 'London', 'Axa')
    #
    # empleado = my_company.change_department_name('IT')
    #
    #
    # count = 0
    # while count < len(empleado):
    #     if empleado is not None:
    #         # print(empleado[count].employee_name)
    #         # print(empleado[count].employee_age)
    #         print(empleado[count].department_name)
    #
    #     count += 1

    my_business = ContextualMenu()
    my_business.show_menu()
