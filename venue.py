from utils import _api_request,set_api_key
import unittest


class Venue(object):
    def __init__(self,id : int = None) -> None:
        end_url = f"venues/{id}"
        json = _api_request(end_url=end_url)["data"]
        self.id = id
        self.slug = json["slug"]
        self.city = json["city"]
        self.name = json["stadium"]
        self.capacity = json["stadium_capacity"]
        self.country_name = json["country_name"]
        pass

class Tests(unittest.TestCase):
    def test_venue(self):
        set_api_key("6267713524msh3531ca742782374p1f47e4jsn09499b89e398")
        v = Venue(id = 1)
        assert(v.id == 1)
        assert(v.slug == "southampton-st-marys-stadium")
        assert(v.city["en"] == "Southampton")
        assert(v.capacity == 32500)
        assert(v.country_name == "England")

unittest.main()