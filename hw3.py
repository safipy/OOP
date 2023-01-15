class Bank():
    def __init__(self, name, balance):
        self._name = name
        self._balance = balance

    def __str__(self):
        return f" {self._name} {self._balance}"

    def moneyX(self, amount):
        self._balance += amount
        print(f'{amount} added to {self._name}\'s account. New balance: {self._balance}')

    def _kill(self, reset):
        if reset == 'yes':
            print(f'Your account has been reset.'
                  f' \nYour balance = {self._balance - self._balance}  ')
        elif reset == 'no':
            print(f'Your balance = {self._balance}')
        else:
            print(f'Wrong Command !!! ')

    def __jeckpot(self):
        jeckpot = 10
        print(f'{self._balance * jeckpot}')

    def _general(self):
        self._balance = my_account._balance + new_account._balance
        print(f'Your balance update! Now is = {self._balance} ')

my_account = Bank('John Snow', 100)
print(f'Account: {my_account._name}, Balance: {my_account._balance}')

new_account = Bank('Endrew Minyard ', 100)
print(f'Account: {new_account._name}, Balance: {new_account._balance}')

amount = input("Enter amount to add: ")
my_account.moneyX(int(amount))

reset = input("Do you want to reset your account ? ")
my_account._kill(str(reset).lower())

my_account._Bank__jeckpot()
#print(dir(Bank))

my_account._general()
new_account._general()