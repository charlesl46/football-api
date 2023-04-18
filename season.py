from utils import _api_request
from league import League
from event import Event
from team import Team


class Season(object):
    def __init__(self,json = None,id = None,league_id = None,year_start = None,year_end = None) -> None:
        if id == None and league_id == None and year_start == None and year_end == None:
            self.id = json["id"]
            self.name = json["name"]
            self.year_start = json["year_start"]
            self.year_end = json["year_end"]
            self.league_id = json["league"]["id"]
        elif json == None and id != None and league_id != None:
            end_url = "seasons/search"
            querystring = {"year_start":year_start,"league_id":league_id,"year_end":year_end}  
            json = _api_request(end_url=end_url,querystring=querystring,type = "POST")["data"][0]
            self.__init__(json = json)
        elif id != None:
            end_url = f"seasons/{id}"
            json = _api_request(end_url=end_url)["data"]
            self.__init__(json = json)     
        pass

    @property
    def league(self):
        return League(id = self.league_id)

    @property
    def events(self):
        res = []
        end_url = f"seasons/{self.id}/events"
        json = _api_request(end_url=end_url)["data"]
        for event_json in json:
            res.append(Event(json = event_json))
        return res
    
    @property
    def teams(self) -> list[Team]:
        res = []
        end_url = f"seasons/{self.id}/teams"
        json = _api_request(end_url=end_url)["data"]
        for team_json in json:
            res.append(Team(json = team_json))
        return res


