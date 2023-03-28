import json
import requests

key = "a2ac39580c2a4088b301d07ad7c093dd"


class Response:
    def __init__(self, data):
        self.data = data.split(",")
        self.response = requests.get(f"https://api.opencagedata.com/geocode/v1/json?q="
                                     f"{self.data[0]}+{self.data[1]}&key={key}&language=id"
                                     f"&pretty=1")
        self.result()

    def result(self):
        result = self.response.json()["results"][0]["geometry"]
        result_2 = self.response.json()["results"][0]["formatted"]
        result_3 = self.response.json()["results"][0]["annotations"]["DMS"]
        result_4 = self.response.json()["results"][0]["components"]
        result_5 = self.response.json()['results'][0]["annotations"]['OSM']['url']
        result_6 = self.response.json()["results"][0]["annotations"]["timezone"]["short_name"]
        result['url'] = result_5
        result["formatted"] = result_2
        result["coord"] = result_3
        result["test"] = result_4
        result["time_zone"] = result_6

        with open("geolocation.json", 'w') as file:
            file_ = json.dumps(result, indent=4)
            file.write(file_)
        with open("test.json", 'w') as file_total:
            file = json.dumps(self.response.json(), indent=4)
            file_total.write(file)

    @staticmethod
    def latitude_():
        with open('geolocation.json', 'r') as file:
            file = json.load(file)
            geo_data = list()
            geo_data.append(file['lat'])
            geo_data.append(file['lng'])
            return geo_data

    @staticmethod
    def content_main():
        with open("geolocation.json",'r') as file:
            file_ = json.load(file)
            return file_

    def content_formated(self):
        return self.content_main()['formatted']

    def content_map(self):
        return self.content_main()['url']

    def time_zone(self):
        return self.content_main()["time_zone"]


