def response_message(input_message):
    message = input_message.lower()

    if message == 'Hello':
        return 'Hello too'
    elif message == 'nice':
        return 'nice too'
    else:
        return 'without nothing to response you'