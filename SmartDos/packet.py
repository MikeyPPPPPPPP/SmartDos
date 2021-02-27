import json

class packet:
    def __init__(self):
        self.cookie = ""
        self.user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
        self.methoud = "get"
        self.timeout = 1
        self.url = ""
        self.port = 1
        self.data = ""

    def build(self):
        file = open("settings.json", "r")
        contents = json.load(file)
        contents["cookie"] = self.cookie
        contents["user_agent"] = self.user_agent
        contents["methoud"] = self.methoud
        contents["timeout"] = self.timeout
        contents["url"] = self.url+':'+str(self.port)
        contents["port"] = self.port
        contents["data"] = self.data
        file.close()
        updated_file = open("settings.json", "w")
        json.dump(contents, updated_file, indent = 4)
        updated_file.close()

"""

{
    "cookie":"",
    "user_agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
    "methoud":"",
    "url":"",
    "port":1,
    "data":""
}
"""
