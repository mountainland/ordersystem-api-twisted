from customer.functions import create_customer

# TODO: move this to functions


class Customer:
    def __init__(self, FirstName, LastName, PhoneNumber, Email, Balance=0, Id=0):
        self.FirstName = FirstName
        self.LastName = LastName
        self.PhoneNumber = PhoneNumber
        self.Email = Email
        self.Balance = Balance
        self.Id = Id

    def DumpCustomer(self):
        Id = create_customer(
            {
                "firstname": self.FirstName,
                "lastname": self.LastName,
                "phonenumber": self.PhoneNumber,
                "email": self.Email,
                "balance": self.Balance,
            }
        )
        return Id
