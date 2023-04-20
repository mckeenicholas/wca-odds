import csv
import competitor


def read_db(persons: dict, event: str, year_cutoff=2022):
    with open("../WCA_export_Results.tsv", newline='', encoding='utf8') \
            as results_db:
        reader = csv.reader(results_db, delimiter='\t')
        next(reader)  # skip the header row
        for items in reader:
            if any(key in items[7] for key in persons.keys()) \
                    and items[1] == event and int(items[0][-4:]) >= year_cutoff:
                print('\t'.join(items))
                match items[9]:
                    case 'a':
                        persons[items[7]].add_result(parse_ints(items[10:15]))
                    case 'm':
                        persons[items[7]].add_result(parse_ints(items[10:13]))
                    case '3':
                        persons[items[7]].add_result(parse_ints(items[10:13]))


def parse_ints(lst: list):
    return [int(numeric_string) for numeric_string in lst]


if __name__ == "__main__":
    c = competitor.Competitor("Nick", "2016KOLA02", 0)
    person = {"2016KOLA02": c}
    read_db(person, "333", 2020)
    print(person["2016KOLA02"].results)
    print(person["2016KOLA02"].simulate_times(1000))
