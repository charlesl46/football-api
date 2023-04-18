from utils import _api_request,FOOTBALL_ID


class Player(object):
    def __init__(self,json : dict = None,id : str = None,team_id : str = None, market_value_min : str = None, market_value_max : str = None, shirt_number : int = None,preferred_foot : str = None,age_min : int = None,age_max : int = None,position : str = None,nationality_code : str = None, name : str= None) -> None:
        if id == None and team_id == None and market_value_max == None and market_value_min == None and shirt_number == None and preferred_foot == None and age_max == None and age_min == None and position == None and nationality_code == None and name == None:
            self.id = json["id"]
            self.name = json["name"]
            self.age = json["age"]
            self.shirt_number = json["shirt_number"]
            self.slug = json["slug"]
            self.position = json["position"]
            self.preferred_foot = json["preferred_foot"]
            self.nationality_code = json["nationality_code"]
            self.market_currency = json["market_currency"]
            self.market_value = json["market_value"]
            self.has_photo = json["has_photo"]
            if self.has_photo:
                self.photo = json["photo"]
            else:
                self.photo = None
        elif json == None and id == None:
            end_url = "players/search"
            querystring = {"team_id":team_id,"sport_id":FOOTBALL_ID,"market_value_max":market_value_max,"age_max":age_max,"market_value_min":market_value_min,"shirt_number":shirt_number,"preferred_foot":preferred_foot,"name":name,"age_min":age_min,"position":position,"nationality_code":nationality_code}           
            json = _api_request(end_url=end_url,querystring=querystring,type = "POST")["data"][0]
            self.__init__(json = json)
        elif id != None:
            end_url = f"players/{id}"
            json = _api_request(end_url=end_url)["data"]
            self.__init__(json = json)     
        pass

    @property
    def teams(self):
        from team import Team
        end_url = f"players/{self.id}/teams"
        json = _api_request(end_url=end_url)
        print(json)
        json = json["data"]
        res = []
        for team_json in json:
            res.append(Team(team_json))
        return res
            

