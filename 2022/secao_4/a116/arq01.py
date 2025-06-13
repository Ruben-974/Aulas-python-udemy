def create_salutation(salutation):
    def salute(name):
        return f'{salutation}, {name}!'
    return salute

good_morning = create_salutation('Good morning')
good_night = create_salutation('Good night')

print(good_morning('Jack'))
print(good_night('Anne'))