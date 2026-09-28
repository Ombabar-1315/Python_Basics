class PasswordTool:

    @staticmethod
    def is_strong(password):
        if len(password) >= 8 and any(char.isdigit() for char in password):
            return True
        return False

print(PasswordTool.is_strong("hello12"))
print(PasswordTool.is_strong("hello"))
print(PasswordTool.is_strong("python2026"))




