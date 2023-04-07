from customer.functions import ReadCustomers, DumpCustomers, CalcCustomer


class Customer():
    def __init__(self, FirstName, LastName, PhoneNumber, Email, Balance=0, Id=0):
        self.FirstName = FirstName
        self.LastName = LastName
        self.PhoneNumber = PhoneNumber
        self.Email = Email
        self.Balance = Balance
        self.Id = Id

    def json(self):
        return {"FirstName": self.FirstName, "LastName": self.LastName, "Balance": self.Balance}

    def DumpCustomer(self):
        customers = ReadCustomers()
        Id = len(customers["customers"])
        self.Id = Id
        customers["customers"].append(
            {"FirstName": self.FirstName, "LastName": self.LastName, "PhoneNumber": self.PhoneNumber, "Email": self.Email, "Balance": self.Balance})
        DumpCustomers(customers)
        return Id

    def CalcBalance(self):
        self.Balance = CalcCustomer(self.Id)

    def PutBalance(self, balance):
        self.Balance = balance

    def SetBalance(self, balance) -> None:
        self.Balance = self.Balance + balance

    def GetBalance(self) -> int:
        return self.Balance
