from bale import MenuKeyboardButton, MenuKeyboardMarkup

def menuComponents(data: list) -> MenuKeyboardMarkup:
    markup = MenuKeyboardMarkup()
    for component in data:
        markup.add(MenuKeyboardButton(component))
        
    return markup