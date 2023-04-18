from utils import _api_request
from team import Team
from venue import Venue

class Event(object):
    """A sports event, you can initialize it with an id"""
    def __init__(self,json : dict = None,id : int = None) -> None:
        if id == None:
            self.id = json["id"]
            self.home_team_id = json["home_team_id"]
            self.away_team_id = json["away_team_id"]
            self.venue_id = json["venue_id"]
            self.referee_id = json["referee_id"]
            self.slug = json["slug"]
            self.name = json["name"]
            self.status = json["status"]
            self.status_more = json["status_more"]
            self.time_details = json["time_details"]
            self.start_at = json["start_at"]
        elif json == None:
            self.id = id
            end_url = f"events/{id}"
            json = _api_request(end_url)["data"]
            self.__init__(json = json, id = None)

    @property
    def home_team(self) -> Team:
        return Team(id = self.home_team_id)

    @property
    def venue(self):
        raise NotImplementedError
    
    @property
    def referee(self):
        raise NotImplementedError

    @property
    def venue(self):
        return Venue(id = self.venue_id)

    @property
    def away_team(self) -> Team:
        return Team(id = self.away_team_id)
    

    
