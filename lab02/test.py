def cake():
    print("beets")

    def pie():
        print("sweets")
        return "cake"

    return pie


chocolate = cake()
print("---------")
more_chocolate, more_cake = chocolate(), cake
