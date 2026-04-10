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
        recall = self.tp / (self.tp + self.fn) if (self.tp + self.fn) > 0 else 0
        precision = self.tp / (self.tp + self.fp) if (self.tp + self.fp) > 0 else 0
        accuracy = (self.tp + self.tn) / (self.tp + self.fp + self.fn + self.tn) if (self.tp + self.fp + self.fn + self.tn) > 0 else 0
        f1_score = 2 * (precision * recall) / (precision + recall) if (precision + recall) > 0 else 0

        path = os.path.join("results", f"{self.name}_report.txt")
        with open(path, "w") as f:
            f.write(f"Report for {self.name}\n")
            f.write(f"True Positives: {self.tp}\n")
            f.write(f"False Positives: {self.fp}\n")
            f.write(f"False Negatives: {self.fn}\n")
            f.write(f"True Negatives: {self.tn}\n")
            f.write(f"Recall: {recall:.2f}\n")
            f.write(f"Precision: {precision:.2f}\n")    
            f.write(f"Accuracy: {accuracy:.2f}\n")
            f.write(f"F1 Score: {f1_score:.2f}\n")