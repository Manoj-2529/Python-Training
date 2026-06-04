def washhands():
    print("Washing Hands")
def servefood():
    print("Serve Food")
def eatfood():
    washhands()
    servefood()
    print("Eat food")
    washhands()
eatfood()