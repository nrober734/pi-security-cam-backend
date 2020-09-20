def update_inventory_state(input_items: dict, state_inventory_dict: dict, operation: str) -> dict:
    #   Operation: 'add' or 'remove'

    for item_name in input_items:
        item_count = input_items[item_name]

        if operation == 'add':

            add_value = state_inventory_dict[item_name]+item_count if state_inventory_dict.get(item_name) else item_count

            update_entry = {item_name: add_value}
            print(update_entry)
            state_inventory_dict.update(update_entry)

        elif operation == 'remove':

            remove_value = state_inventory_dict[item_name]-item_count if state_inventory_dict.get(item_name) else item_count

            update_entry = {item_name, remove_value}
            state_inventory_dict.update(update_entry)
        else:
            raise ValueError('Operation must be add or remove')

    return state_inventory_dict
