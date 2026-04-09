import os

class Report:
    def __init__(self, name: str):
        self.name = name
        self.tp = 0
        self.fp = 0
        self.fn = 0
        self.tn = 0

    def true_positive(self):
        self.tp += 1

    def false_positive(self):
        self.fp += 1

    def false_negative(self):
        self.fn += 1

    def true_negative(self):
        self.tn += 1

    def save_report(self):
        path = os.path.join("results", f"{self.name}_report.txt")
        with open(path, "w") as f:
            f.write(f"Report for {self.name}\n")
            f.write(f"True Positives: {self.tp}\n")
            f.write(f"False Positives: {self.fp}\n")
            f.write(f"False Negatives: {self.fn}\n")
            f.write(f"True Negatives: {self.tn}\n")
