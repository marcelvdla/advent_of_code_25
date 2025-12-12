class button:
    def __init__(self, action: tuple[int]):
        self.action = action


    def __str__(self):
        return str(self.action)


    def press(self, state : str):
        new_state = ""
        for i in range(len(state)):
            if i in self.action:
                new_state += self.switch(state[i])
            else:
                new_state += state[i]
        return new_state


    def switch(self, light : str):
        if (light == '.'):
            return "#"
        return "."
