def response(input_message):
    message = input_message.lower()

    if message == 'nice':
        return 'Very nice'
    elif message == 'hello':
        return 'Hello there'
    else:
        return 'Cool!'
