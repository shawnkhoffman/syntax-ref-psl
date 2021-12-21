class topic():
    def __init__(self, option, chosen_topic):
        self.option = option
        self.chosen_topic = chosen_topic

    def selection(self):
        return self.option

    def choice(self):
        return self.chosen_topic


class selection(topic):
    def __init__(self, d, option, chosen_topic):
        super().__init__(option, chosen_topic)
        self.d = d

    def query_topics(self):
        for self.k, self.v in self.d.items():
            if self.option == self.k or self.option == self.v:
                self.chosen_topic = self.v
                return self.chosen_topic
            else:
                continue
