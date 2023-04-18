from utils import _api_request,set_api_key,FOOTBALL_ID
import unittest
from typing import TYPE_CHECKING


class Team(object):
    def __init__(self,json : dict = None,id : str = None, country : str = None, name : str= None) -> None:
        if id == None and country == None and name == None:
            self.id = json["id"]
            self.name = json["name"]
            self.slug = json["slug"]
            self.manager_id = json["manager_id"]
            self.venue_id = json["venue_id"]
            self.has_logo = json["has_logo"]
            self.gender = json["gender"]
            if self.has_logo:
                self.logo = json["logo"]
            else:
                self.logo = None
        elif json == None and id == None:
            end_url = "teams/search"
            querystring = {"country": country,"name":name,"sport_id":FOOTBALL_ID}
            json = _api_request(end_url=end_url,querystring=querystring,type = "POST")["data"][0]
            self.__init__(json = json)
        elif id != None:
            end_url = f"teams/{id}"
            json = _api_request(end_url=end_url)["data"]
            self.__init__(json = json)     
        pass

    @property
    def players(self):
        from player import Player
        end_url = f"teams/{self.id}/players"
        players = _api_request(end_url=end_url)["data"]
        res = []
        for player_json in players:
            res.append(Player(json = player_json))
        return res
    
    @property
    def manager(self):
        from manager import Manager
        return Manager(id = self.manager_id)


class Tests(unittest.TestCase):
    def test_team_by_id(self):
        set_api_key("6267713524msh3531ca742782374p1f47e4jsn09499b89e398")
        id = 139
        json = {
        "data": [
            {
            "id": 139,
            "sport_id": 1,
            "category_id": 32,
            "venue_id": 82,
            "manager_id": 1825,
            "slug": "real-madrid",
            "name": "Real Madrid",
            "has_logo": True,
            "logo": "https://tipsscore.com/resb/team/real-madrid.png",
            "name_translations": {
                "en": "Real Madrid",
                "ru": "Реал Мадрид",
                "de": "Real Madrid",
                "es": "Real Madrid CF",
                "fr": "Real Madrid",
                "zh": "皇家马德里",
                "tr": "Real Madrid",
                "el": "Ρεάλ Μαδρίτης",
                "it": "Real Madrid",
                "nl": "Real Madrid",
                "pt": "Real Madrid CF"
            },
            "name_short": "Real Madrid",
            "name_full": "Real Madrid",
            "name_code": "RMA",
            "has_sub": False,
            "gender": "M",
            "is_nationality": False,
            "country_code": "ESP",
            "country": "Spain",
            "flag": "spain",
            "foundation": None,
            "details": None
            },
            {
            "id": 3950,
            "sport_id": 1,
            "category_id": 32,
            "venue_id": 1447,
            "manager_id": 8020,
            "slug": "cd-tacon",
            "name": "Real Madrid Femenino",
            "has_logo": True,
            "logo": "https://tipsscore.com/resb/team/cd-tacon.png",
            "name_translations": {
                "en": "Real Madrid Femenino",
                "ru": "Cd Tacon",
                "zh": "塔孔",
                "el": "Ρεάλ",
                "pt": "Real Madrid CF",
                "de": "Real Madrid CF",
                "fr": "Real Madrid CF"
            },
            "name_short": "Real Madrid Femenino",
            "name_full": "Real Madrid Femenino",
            "name_code": "RMA",
            "has_sub": False,
            "gender": "F",
            "is_nationality": False,
            "country_code": "ESP",
            "country": "Spain",
            "flag": "spain",
            "foundation": None,
            "details": None
            },
            {
            "id": 3988,
            "sport_id": 1,
            "category_id": 32,
            "venue_id": 1447,
            "manager_id": 1434,
            "slug": "real-madrid-castilla",
            "name": "Real Madrid Castilla",
            "has_logo": True,
            "logo": "https://tipsscore.com/resb/team/real-madrid-castilla.png",
            "name_translations": {
                "en": "Real Madrid Castilla",
                "ru": "Реал Мадрид Б",
                "de": "Real Madrid B",
                "es": "Real Madrid B",
                "zh": "皇家马德里B队",
                "tr": "Real Madrid (A)",
                "el": "Ρεάλ Μαδρίτης Β΄",
                "nl": "Real Madrid Castilla",
                "pt": "Real Madrid B"
            },
            "name_short": "Real Madrid Castilla",
            "name_full": "Real Madrid Castilla",
            "name_code": "RMA",
            "has_sub": False,
            "gender": "M",
            "is_nationality": False,
            "country_code": "ESP",
            "country": "Spain",
            "flag": "spain",
            "foundation": None,
            "details": None
            },
            {
            "id": 10220,
            "sport_id": 1,
            "category_id": 32,
            "venue_id": None,
            "manager_id": 9809,
            "slug": "real-madrid-u19",
            "name": "Real Madrid U19",
            "has_logo": True,
            "logo": "https://tipsscore.com/resb/team/real-madrid-u19.png",
            "name_translations": {
                "en": "Real Madrid U19",
                "ru": "Реал Мадрид",
                "de": "Real Madrid",
                "es": "Real Madrid",
                "zh": "皇家马德里",
                "tr": "Real Madrid",
                "el": "Ρεάλ Μαδρίτης",
                "it": "Real Madrid",
                "nl": "Real Madrid",
                "pt": "Real Madrid"
            },
            "name_short": "Real Madrid U19",
            "name_full": "Real Madrid U19",
            "name_code": "RMA",
            "has_sub": False,
            "gender": "M",
            "is_nationality": False,
            "country_code": "ESP",
            "country": "Spain",
            "flag": "spain",
            "foundation": None,
            "details": None
            },
            {
            "id": 105708,
            "sport_id": 1,
            "category_id": 32,
            "venue_id": None,
            "manager_id": None,
            "slug": "real-madrid-u18",
            "name": "Real Madrid U18",
            "has_logo": False,
            "logo": "https://tipsscore.com/resb/no-league.png",
            "name_translations": {
                "en": "Real Madrid U18"
            },
            "name_short": "Real Madrid",
            "name_full": "Real Madrid U18",
            "name_code": "RMA",
            "has_sub": False,
            "gender": None,
            "is_nationality": False,
            "country_code": "ESP",
            "country": "Spain",
            "flag": "spain",
            "foundation": None,
            "details": None
            },
            {
            "id": 117725,
            "sport_id": 1,
            "category_id": 32,
            "venue_id": None,
            "manager_id": None,
            "slug": "real-madrid-c",
            "name": "Real Madrid C",
            "has_logo": False,
            "logo": "https://tipsscore.com/resb/no-league.png",
            "name_translations": {
                "en": "Real Madrid C",
                "ru": "Реал Мадрид С",
                "zh": "皇家马德里队C",
                "el": "Ρεάλ Μαδρίτης Γ'",
                "it": "Real Madrid"
            },
            "name_short": "R. Madrid C",
            "name_full": "Real Madrid C",
            "name_code": "RSC",
            "has_sub": False,
            "gender": "M",
            "is_nationality": False,
            "country_code": "ESP",
            "country": "Spain",
            "flag": "spain",
            "foundation": None,
            "details": None
            }
        ],
        "meta": {
            "current_page": 1,
            "from": 1,
            "per_page": 100,
            "to": 6
        }
        }["data"][0]
        t = Team(id = 139)
        assert(t.id == id)
        assert(t.slug == json["slug"])
        assert(t.manager_id == json["manager_id"])
        assert(t.logo == json["logo"])

    def test_team_by_country_name(self):
        set_api_key("6267713524msh3531ca742782374p1f47e4jsn09499b89e398")
        id = 139
        json = {
        "data": [
            {
            "id": 139,
            "sport_id": 1,
            "category_id": 32,
            "venue_id": 82,
            "manager_id": 1825,
            "slug": "real-madrid",
            "name": "Real Madrid",
            "has_logo": True,
            "logo": "https://tipsscore.com/resb/team/real-madrid.png",
            "name_translations": {
                "en": "Real Madrid",
                "ru": "Реал Мадрид",
                "de": "Real Madrid",
                "es": "Real Madrid CF",
                "fr": "Real Madrid",
                "zh": "皇家马德里",
                "tr": "Real Madrid",
                "el": "Ρεάλ Μαδρίτης",
                "it": "Real Madrid",
                "nl": "Real Madrid",
                "pt": "Real Madrid CF"
            },
            "name_short": "Real Madrid",
            "name_full": "Real Madrid",
            "name_code": "RMA",
            "has_sub": False,
            "gender": "M",
            "is_nationality": False,
            "country_code": "ESP",
            "country": "Spain",
            "flag": "spain",
            "foundation": None,
            "details": None
            },
            {
            "id": 3950,
            "sport_id": 1,
            "category_id": 32,
            "venue_id": 1447,
            "manager_id": 8020,
            "slug": "cd-tacon",
            "name": "Real Madrid Femenino",
            "has_logo": True,
            "logo": "https://tipsscore.com/resb/team/cd-tacon.png",
            "name_translations": {
                "en": "Real Madrid Femenino",
                "ru": "Cd Tacon",
                "zh": "塔孔",
                "el": "Ρεάλ",
                "pt": "Real Madrid CF",
                "de": "Real Madrid CF",
                "fr": "Real Madrid CF"
            },
            "name_short": "Real Madrid Femenino",
            "name_full": "Real Madrid Femenino",
            "name_code": "RMA",
            "has_sub": False,
            "gender": "F",
            "is_nationality": False,
            "country_code": "ESP",
            "country": "Spain",
            "flag": "spain",
            "foundation": None,
            "details": None
            },
            {
            "id": 3988,
            "sport_id": 1,
            "category_id": 32,
            "venue_id": 1447,
            "manager_id": 1434,
            "slug": "real-madrid-castilla",
            "name": "Real Madrid Castilla",
            "has_logo": True,
            "logo": "https://tipsscore.com/resb/team/real-madrid-castilla.png",
            "name_translations": {
                "en": "Real Madrid Castilla",
                "ru": "Реал Мадрид Б",
                "de": "Real Madrid B",
                "es": "Real Madrid B",
                "zh": "皇家马德里B队",
                "tr": "Real Madrid (A)",
                "el": "Ρεάλ Μαδρίτης Β΄",
                "nl": "Real Madrid Castilla",
                "pt": "Real Madrid B"
            },
            "name_short": "Real Madrid Castilla",
            "name_full": "Real Madrid Castilla",
            "name_code": "RMA",
            "has_sub": False,
            "gender": "M",
            "is_nationality": False,
            "country_code": "ESP",
            "country": "Spain",
            "flag": "spain",
            "foundation": None,
            "details": None
            },
            {
            "id": 10220,
            "sport_id": 1,
            "category_id": 32,
            "venue_id": None,
            "manager_id": 9809,
            "slug": "real-madrid-u19",
            "name": "Real Madrid U19",
            "has_logo": True,
            "logo": "https://tipsscore.com/resb/team/real-madrid-u19.png",
            "name_translations": {
                "en": "Real Madrid U19",
                "ru": "Реал Мадрид",
                "de": "Real Madrid",
                "es": "Real Madrid",
                "zh": "皇家马德里",
                "tr": "Real Madrid",
                "el": "Ρεάλ Μαδρίτης",
                "it": "Real Madrid",
                "nl": "Real Madrid",
                "pt": "Real Madrid"
            },
            "name_short": "Real Madrid U19",
            "name_full": "Real Madrid U19",
            "name_code": "RMA",
            "has_sub": False,
            "gender": "M",
            "is_nationality": False,
            "country_code": "ESP",
            "country": "Spain",
            "flag": "spain",
            "foundation": None,
            "details": None
            },
            {
            "id": 105708,
            "sport_id": 1,
            "category_id": 32,
            "venue_id": None,
            "manager_id": None,
            "slug": "real-madrid-u18",
            "name": "Real Madrid U18",
            "has_logo": False,
            "logo": "https://tipsscore.com/resb/no-league.png",
            "name_translations": {
                "en": "Real Madrid U18"
            },
            "name_short": "Real Madrid",
            "name_full": "Real Madrid U18",
            "name_code": "RMA",
            "has_sub": False,
            "gender": None,
            "is_nationality": False,
            "country_code": "ESP",
            "country": "Spain",
            "flag": "spain",
            "foundation": None,
            "details": None
            },
            {
            "id": 117725,
            "sport_id": 1,
            "category_id": 32,
            "venue_id": None,
            "manager_id": None,
            "slug": "real-madrid-c",
            "name": "Real Madrid C",
            "has_logo": False,
            "logo": "https://tipsscore.com/resb/no-league.png",
            "name_translations": {
                "en": "Real Madrid C",
                "ru": "Реал Мадрид С",
                "zh": "皇家马德里队C",
                "el": "Ρεάλ Μαδρίτης Γ'",
                "it": "Real Madrid"
            },
            "name_short": "R. Madrid C",
            "name_full": "Real Madrid C",
            "name_code": "RSC",
            "has_sub": False,
            "gender": "M",
            "is_nationality": False,
            "country_code": "ESP",
            "country": "Spain",
            "flag": "spain",
            "foundation": None,
            "details": None
            }
        ],
        "meta": {
            "current_page": 1,
            "from": 1,
            "per_page": 100,
            "to": 6
        }
        }["data"][0]
        t = Team(country = "Spain",name = "Real Madrid")
        assert(t.id == id)
        assert(t.slug == json["slug"])
        assert(t.manager_id == json["manager_id"])
        assert(t.logo == json["logo"])

#unittest.main()

set_api_key("6267713524msh3531ca742782374p1f47e4jsn09499b89e398")
t = Team(id = 137)

for player in t.players:
    print(player.teams[0])