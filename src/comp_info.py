import requests
import competitor


def get_wcif(competition: str, event: str, event_type: str):
    url = "https://www.worldcubeassociation.org/api/v0/competitions/"\
          + competition + "/wcif/public"
    response = requests.get(url)
    competitors_in_event = []
    for person in response.json()['persons']:
        if person['registration'] is not None \
                and event in person['registration']['eventIds']:
            rank = get_pb_rank(person, event, event_type)
            if rank is not None:
                comp = competitor.Competitor(person['name'].encode('ascii',
                                                                   'replace')
                                             .decode(),
                                             person['wcaId'],
                                             rank)
                competitors_in_event.append(comp)
    return competitors_in_event


def get_pb_rank(person, event, event_type):
    for result in person['personalBests']:
        if result['eventId'] == event\
                and result['type'] == event_type:
            return result['worldRanking']


def get_psych(comp: str, event: str, type: str, top_num: int):
    persons = get_wcif(comp, event, type)
    persons.sort(key=lambda x: x.rank);
    return persons[:top_num]


if __name__ == "__main__":
    comps = get_wcif("CanadianChampionship2023", "333", "average")
    comps.sort(key=lambda x: x.rank)
    for comp in comps:
        print(comp)

