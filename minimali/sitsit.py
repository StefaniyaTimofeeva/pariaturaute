def reset_inv(inventory):
    if isinstance(inventory, list):
        return []
    elif isinstance(inventory, dict):
        return {}
    elif isinstance(inventory, str):
        return 'nothing in inventory'
    elif isinstance(inventory, bool):
        return False
    else:
        return 'not inventory type'
