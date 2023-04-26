import comp_info
import db_reader as db

num_attempts = {"average": 5, "mean": 3, "best": 3}


def calculate_odds(comp: str, event: str, results_type: str, round_type: str, num_consider=16, num_simulations=1000):
    return_list = comp_info.get_psych(comp, event, results_type, num_consider)
    competitors_dict = {}
    for competitor in return_list:
        competitors_dict[competitor.wca_id] = competitor
    db.read_db(competitors_dict, event)
    for competitor in competitors_dict.values():
        print(competitor.global_average())
    print("Results Fetched, Simulating Competitions")
    for i in range(num_simulations):
        results = []
        for competitor in competitors_dict.values():
            results.append((competitor, get_average(competitor.simulate_times(
                num_attempts[round_type]), round_type)))
        results.sort(key=lambda x: x[1])
        results[0][0].num_wins += 1
        results[0][0].num_podium += 1
        results[1][0].num_podium += 1
        results[2][0].num_podium += 1
    for i, competitor in enumerate(results):
        print(f"{i + 1}. {competitor[0].name.ljust(30)} "
              f"win% {(competitor[0].num_wins / num_simulations) * 100:6.2f} "
              f"podium% {(competitor[0].num_podium / num_simulations) * 100:6.2f}")


def get_average(results: list, round_type: str):
    num_dnf = results.count(-1)
    results.sort()

    if round_type == "average":
        if num_dnf > 1:
            return -1
        elif num_dnf > 0:
            return (results[2] + results[3] + results[4]) // 3
        return (results[1] + results[2] + results[3]) // 3
    elif round_type == "mean":
        if num_dnf > 0:
            return -1
        return (results[0] + results[1] + results[2]) // 3
    elif round_type == "best":
        if num_dnf == 3:
            return -1
        for i in range(3):
            if results[i] != -1:
                return results[i]


if __name__ == "__main__":
    calculate_odds("HalifaxFavourites2023", "333", "average", "average", 16, 10000)
