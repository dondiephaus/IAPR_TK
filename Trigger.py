class Trigger:
    def __init__(self, probability, impact, edge_weight):
        self.probability = probability
        self.impact = impact
        self.weight = edge_weight
        self.risk_value = self.calculate_risk()

    def calculate_risk(self):
        return self.impact * self.probability * self.weight
