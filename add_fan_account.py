'''
    function add_fan_account():
        - ask to input the name
        - ask to input the nickname
        - check if the nickname doesn't already exist (if the fan already exists, the function stops - use the function is_nickname_new from the db module)
        - calls the function add_fan_account (using the function is_nickname_new from the db module)
'''
def add_fan_account(db):

    # add your code here

    db.add_fan_account(fan_nickname, fan_name)
    return 0
