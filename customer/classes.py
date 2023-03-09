from customer.functions import ReadCustomers, DumpCustomers


class Customer():
    def __init__(self, FirstName, LastName, Balance=0):
        self.FirstName = FirstName
        self.LastName = LastName
        self.Balance = Balance

    def json(self):
        return {"FirstName": self.FirstName, "LastName": self.LastName, "Balance": self.Balance}

    def DumpCustomer(self):
        customers = ReadCustomers()
        customers["customers"].append(self.json)
        DumpCustomers(customers)

    def PutBalance(self, balance):
        self.Balance = balance

    def SetBalance(self, balance) -> None:
        self.Balance = self.Balance + balance

    def GetBalance(self) -> int:
        return self.Balance
