def validation_password(password):
    if len(password) >=8:
        if any(char.isdigit() for char in password):
               if any(char.isupper() for char in password):
                    if any(char.islower() for char in password):
                         if any(char in '!@#$%^&*()' for char in password)
