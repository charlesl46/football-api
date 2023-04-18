from utils import _api_request,FOOTBALL_ID
from team import Team

class Manager(object):
    def __init__(self,json : dict = None,id : str = None,name : str = None,nationality_code : str = None) -> None:
        if id == None and nationality_code == None and name == None:
            self.id = json["id"]
            self.name = json["name"]
            self.slug = json["slug"]
            self.date_birth = json["date_birth"]
            self.nationality_code = json["nationality_code"]
            self.has_photo = json["has_photo"]
            if self.has_photo:
                self.photo = json["photo"]
            else:
                self.photo = None
            self.team_json = json["team"]
        elif json == None and id == None:
            end_url = "managers/search"
            querystring = {"name" : name,"sport_id":FOOTBALL_ID,"name":name,"nationality_code":nationality_code}           
            json = _api_request(end_url=end_url,querystring=querystring,type = "POST")["data"][0]
            self.__init__(json = json)
        elif id != None:
            end_url = f"managers/{id}"
            json = _api_request(end_url=end_url)["data"]
            self.__init__(json = json)     
        pass

    @property
    def team(self) -> Team:
        return Team(json = self.team_json)
