from datetime import date


class Contract:
    creation_date = ""
    employee = None
    # Company information
    # ---------------------------
    company_name = ''
    company_cif = ''

    # Contract constructor
    def __init__(self, employee, company_name, company_cif):
        today = date.today()
        self.creation_date = today.strftime("%d/%m/%Y")
        self.employee = employee
        self.company_name = company_name
        self.company_cif = company_cif
