class Account(object):

    ID_COUNT = 1

    def __init__(self, name, **kwargs):
        self.id = self.ID_COUNT
        self.name = name
        self.__dict__.update(kwargs)
        Account.ID_COUNT += 1

    def transfer(self, amount):
        self.value += amount


class Bank(object):
    """The bank"""

    def __init__(self):
        self.accounts = []

    def add(self, account):
        self.accounts.append(account)

    def get_account(self, target):
        if isinstance(target, str):
            target_act = next((x for x in self.accounts if x.name == target), None)
        elif isinstance(target, int):
            target_act = next((x for x in self.accounts if x.id == target), None)
        else:
            raise TypeError
        if not target_act:
            return False
        return target_act

    def transfer(self, origin, dest, amount):
        """
            @origin:  int(id) or str(name) of the first account
            @dest:    int(id) or str(name) of the destination account
            @amount:  float(amount) amount to transfer
            @return         True if success, False if an error occured
        """
        origin_act = self.get_account(origin)
        if not origin_act:
            raise ValueError("origin doesn't exist")
        dest_act = self.get_account(dest)
        if not dest_act:
            raise ValueError("dest doesn't exist")

        attri_lst = ["id", "zip", "addr", "name", "value"]
        if not all(x in dir(origin_act) for x in attri_lst) or not all(
            x in dir(dest_act) for x in attri_lst
        ):
            return False
        if any(elem.startswith("b") for elem in dir(origin_act)) or any(
            elem.startswith("b") for elem in dir(dest_act)
        ):
            return False

        if amount < 0 or amount > origin_act.value:
            print(amount, origin_act.value)
            return False
        origin_act.value -= amount
        dest_act.value += amount
        return True

    def fix_account(self, account):
        """
            fix the corrupted account
            @account: int(id) or str(name) of the account
            @return         True if success, False if an error occured
        """
