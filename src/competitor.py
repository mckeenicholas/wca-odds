import numpy as np


class Competitor:
    name: str
    wca_id: str
    rank: int
    num_results: int
    num_dnf: int
    results = []

    def __init__(self, name: str, wca_id: str, rank: int):
        self.name = name
        self.wca_id = wca_id
        self.rank = rank
        num_results, num_dnf = 0, 0

    def add_result(self, results: list):
        self.results.extend(results)

    def __str__(self):
        return f"Name: {self.name}, WCA ID: {self.wca_id} Rank: {self.rank}"

    def simulate_times(self, num: int):
        mu = np.mean(self.results)
        sigma = np.std(self.results, ddof=1)
        return np.random.normal(mu, sigma, num)
