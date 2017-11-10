def checkio(data):
    return data[0] + checkio(data[1:]) if len(data) else 0
