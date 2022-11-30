from Trigger import Trigger

class RiskEvent:
    # constructor method
    def __init__(self, edge_weight, triggers):
        self.edge_weight = edge_weight
        self.triggers = triggers
        self.risk_factor = self.calculate_risk_factor()
        self.weighted_risk = self.calculate_risk()

    def calculate_risk_factor(self):
        result = 0
        for obj in self.triggers:
            result = result + obj.trigger_risk
        return result

    def calculate_risk(self):
        return self.risk_factor * self.edge_weight



