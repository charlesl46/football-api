from utils import _api_request,FOOTBALL_ID
from season import Season
from team import Team

class League(object):
    def __init__(self,json : dict = None, name = None) -> None:
        if name == None :
            self.id = json["id"]
            self.slug = json["slug"]
            self.name_translations = json["name_translations"]
            self.has_logo = json["has_logo"]
            self.logo = None
            if self.has_logo:
                self.logo = json["logo"]
            self.start_date = json["start_date"]
            self.end_date = json["end_date"]
        elif json == None:
            end_url = "leagues/search"
            querystring = {"sport_id" : FOOTBALL_ID, "name" : name}
            json = _api_request(end_url,querystring, type = "POST")["data"][0]
            self.__init__(json = json,name = None,sport_id=None)
        pass
    
    @property
    def teams(self) -> list[Team]:
        return self.latest_season().teams()
    
    @property
    def latest_season(self) -> Season:
        end_url = "seasons/search"
        querystring = {"league_id":self.id}  
        json = _api_request(end_url=end_url,querystring=querystring,type = "POST")["data"][-1]
        return Season(json = json)

    @property
    def seasons(self) -> list[Season]:
        res = []
        end_url = "seasons/search"
        querystring = {"league_id":self.id}  
        json = _api_request(end_url=end_url,querystring=querystring,type = "POST")["data"]
        for season in json:
            res.append(season)
        return res