def add_setting(settings, setting):
    key, value = setting
    key = str(key).lower()
    value = str(value).lower()

    if key in settings:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
    else:
        settings[key] = value
        return f"Setting '{key}' added with value '{value}' successfully!"

def update_setting(settings, setting):
    key, value = setting
    key = str(key).lower()
    value = str(value).lower()

    if key in settings:
        settings.update({key: value})
        return f"Setting '{key}' updated to '{value}' successfully!"
    else:    
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting."

def delete_setting(settings, key):
    key = str(key).lower()

    if key in settings:
        settings.pop(key)
        return f"Setting '{key}' deleted successfully!"
    else:    
        return f"Setting not found!"

def view_settings(settings):
    if not settings:
        return "No settings available."
    else:
        return "Current User Settings:\n" + "\n".join([f"{key.capitalize()}: {value}" for key, value in settings.items()]) + "\n"

# Test Settings Dictionary
test_settings = {
    'theme': 'light',
    'notifications': 'enabled',
}

# Test Cases
print(add_setting(test_settings, ('THEME', 'dark')))  # Should return an error message
print(add_setting(test_settings, ('volume', 'high')))  # Should add and return success message
print(update_setting(test_settings, ('theme', 'dark')))  # Should update and return success message
print(update_setting(test_settings, ('language', 'english')))  # Should return an error message
print(delete_setting(test_settings, 'theme'))  # Should remove and return success message
print(view_settings(test_settings))  # Should display settings and end with a newline
