import pandas as pd

data = pd.read_csv("50_states.csv")


class Data:
    def __init__(self):
        self.data = data
        self.total_correct_guesses = 0
        self.states_already_guessed = []

    def length_of_data(self):
        return len(self.data)

    def update_correct_guesses(self, answer_state):
        for index, row in self.data.iterrows():
            states = row[0].lower()
            answer_state_lower = answer_state.lower()
            if answer_state_lower in states:
                if states not in self.states_already_guessed:
                    self.total_correct_guesses += 1
                    self.states_already_guessed.append(states)
                    country_x = row[1]
                    country_y = row[2]

                    return states, country_x, country_y

#
# d = Data()
#
# print(d.update_correct_guesses())
