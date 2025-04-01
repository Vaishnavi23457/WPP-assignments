class Password_manager:
    def __init__(self):
        self.old_passwords = []

    def get_password(self):
        if self.old_passwords:
            return self.old_passwords[-1]
        return None

    def set_password(self, new_password):
        if new_password not in self.old_passwords:
            self.old_passwords.append(new_password)
            return True
        return False

    def is_correct(self, password):
        return password == self.get_password()


pm = Password_manager()

n=int(input("enter no of testcases:"))
for i in range(n):
    new_password = input("Enter a new password: ")
    if pm.set_password(new_password):
        print("Password changed successfully.")
    else:
        print("Password change failed. The password is either the same as .")

pm.set_password(new_password)
print(pm.get_password())  
print("is_correct :",pm.is_correct(new_password)) 

