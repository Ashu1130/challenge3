def value_from_nested_object(nested_obj, key):
    keys = key.split('/')
    current_obj = nested_obj

    for c in keys:
        if c in current_obj:
            current_obj = current_obj[c]
        else:
            return None

    return current_obj