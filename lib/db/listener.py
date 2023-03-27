class Listener:

    all_listeners = []

    def __init__(self, name,):
        self.name = name
        Listener.all_listeners.append(self)