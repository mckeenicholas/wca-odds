import random
import numpy as np


class Competitor:
    name: str
    wca_id: str
    rank: int
    num_results: int
    num_dnf: int
    num_wins: int
    num_podium: int

    def __init__(self, name: str, wca_id: str, rank: int):
        self.name = name
        self.wca_id = wca_id
        self.rank = rank
        self.num_results, self.num_dnf = 0, 0
        self.num_wins, self.num_podium = 0, 0
        self.results = []

    def add_result(self, results: list):
        self.num_results += len(results)
        for result in results:
            if result == -1:
                self.num_dnf += 1
            else:
                self.results.append(result)

    def __str__(self):
        return f"{self.name}, {self.wca_id}"

    def simulate_times(self, num: int):
        mu = np.mean(self.results)
        sigma = np.std(self.results, ddof=1)
        times = np.random.normal(mu, sigma, num)
        for i in range(num):
            if random.random() < self.dnf_rate():
                times[i] = -1
        return times.tolist()

    def dnf_rate(self):
        if self.num_results == 0:
            return 1
        return self.num_dnf / self.num_results

    def global_average(self):
        return np.mean(self.results)
