import numpy as np
from numpy import random


class Competitor:
    name: str
    wca_id: str
    rank: int
    num_results: int
    num_dnf: int
    num_wins: int
    num_podium: int
    dnf_average_chance: int

    def __init__(self, name: str, wca_id: str, rank: int):
        self.name = name
        self.wca_id = wca_id
        self.rank = rank
        self.num_results, self.num_dnf = 0, 0
        self.num_wins, self.num_podium = 0, 0
        self.results = []
        self.dnf_average_chance = 0

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
        return np.random.normal(mu, sigma, num)

    def dnf_rate(self):
        if self.num_results == 0:
            return 1
        return self.num_dnf / self.num_results

    def generate_stats(self, event_type: str):
        good_average = 1 - self.dnf_rate()
        if event_type == "average":
            self.dnf_average_chance = 1 - ((good_average ** 5) + (5 * (good_average ** 4) * (1 - good_average)))
        elif event_type == "mean":
            self.dnf_average_chance = 1 - (good_average ** 3)
        elif event_type == "best":
            self.dnf_average_chance = (1 - good_average) ** 3

    def global_average(self):
        return np.mean(self.results)
