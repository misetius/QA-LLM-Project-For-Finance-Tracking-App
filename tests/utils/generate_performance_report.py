import os

class PerformanceTestReport:
    def __init__(self, model_name):
        self.model_name = model_name
        self.total_cold_latency_tests = 0
        self.total_warm_latency_tests = 0
        self.cold_latency = 0
        self.warm_latency = 0

    def add_cold_latency(self, latency):
        self.cold_latency += latency
        self.total_cold_latency_tests += 1

    def return_cold_latency(self):
        return self.cold_latency
    
    def add_warm_latency(self, latency):
        self.warm_latency += latency
        self.total_warm_latency_tests += 1

    def return_warm_latency(self):
        return self.warm_latency

    def save_report(self):
        path = os.path.join("results", f"{self.model_name}_performance_report.txt")
        cold_latency_average = self.cold_latency / self.total_cold_latency_tests if self.total_cold_latency_tests > 0 else 0
        warm_latency_average = self.warm_latency / self.total_warm_latency_tests if self.total_warm_latency_tests > 0 else 0

        with open(path, "w") as f:
            f.write(f"Performance Report for {self.model_name}\n")
            f.write(f"Total Cold Latency Tests: {self.total_cold_latency_tests}\n")
            f.write(f"Total Warm Latency Tests: {self.total_warm_latency_tests}\n")
            f.write(f"Average Cold Latency: {cold_latency_average:.2f} seconds\n")
            f.write(f"Average Warm Latency: {warm_latency_average:.2f} seconds\n")

