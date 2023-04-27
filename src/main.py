import time
import comp_info
import numpy as np
import db_reader as db

num_attempts = {"average": 5, "mean": 3, "best": 3}


def calculate_odds(comp: str, event: str, results_type: str, round_type: str, num_consider=16, num_simulations=1000):
    return_list = comp_info.get_psych(comp, event, results_type, num_consider)
    competitors_dict = {}
    for competitor in return_list:
        competitors_dict[competitor.wca_id] = competitor
    db.read_db(competitors_dict, event)
    print("Results Fetched, Simulating Competitions")
    valid_competitors = get_comp_with_results(competitors_dict, round_type)
    start_time = time.time()
    for i in range(num_simulations):
        results = []
        for competitor in valid_competitors:
            if np.random.rand() < competitor.dnf_average_chance:
                continue
            results.append((competitor, get_average(competitor.simulate_times(num_attempts[round_type]), round_type)))
        results.sort(key=lambda x: x[1])
        if len(results) > 0:
            results[0][0].num_wins += 1
            results[0][0].num_podium += 1
            if len(results) > 1:
                results[1][0].num_podium += 1
                if len(results) > 2:
                    results[2][0].num_podium += 1
    valid_competitors.sort(key=lambda x: x.num_wins, reverse=True)
    print(f"Finished {num_simulations} simulations in {time.time() - start_time:3.2} seconds")
    print(f"Predictions for {comp}:")
    for i, competitor in enumerate(valid_competitors):
        print(f"{str(i + 1).ljust(2)} {competitor.name.ljust(30)} "
              f"win%{(competitor.num_wins / num_simulations) * 100:6.2f}  "
              f"podium%{(competitor.num_podium / num_simulations) * 100:6.2f}")


def get_average(results: list, round_type: str):
    results.sort()
    if round_type == "average":
        return (results[1] + results[2] + results[3]) / 3
    elif round_type == "mean":
        return np.mean(results)
    elif round_type == "best":
        return results[0]


def get_comp_with_results(competitors_dict: dict, event_type):
    results = []
    for competitor in competitors_dict.values():
        if competitor.num_results != 0:
            results.append(competitor)
            competitor.generate_stats(event_type)
    return results


if __name__ == "__main__":
    calculate_odds("CubingUSANationals2023", "333", "average", "average", 16, 10000)
