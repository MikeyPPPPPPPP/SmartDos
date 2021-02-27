import json

class agent:
    def __init__(self):
        self.pattern = ''
        self.agent = ''

    def options(self):
        file = open("useragents.json", "r")
        contents = json.load(file, encoding='utf-8')
        counter = 0
        for x in contents:
            #for y in x['pattern']:
            #    print(y)
            print('['+str(counter)+'] '+x['pattern'])
            counter += 1
        file.close()

    def pick_option(self):
        i = input("option:")
        file = open("useragents.json", "r")
        contents = json.load(file, encoding='utf-8')
        counter = 0
        for x in contents:
            #for y in x['pattern']:
            #    print(y)
            if int(i) == counter:
                self.pattern = str(x['pattern'])
                break
            else:
                counter += 1
        file.close()

    def agentviewer(self):
        file = open("useragents.json", "r")
        contents = json.load(file, encoding='utf-8')
        counter = 0
        for x in contents:
            #for y in x['pattern']:
            #    print(y)
            #print(self.pattern)
            if x['pattern'] == self.pattern:
                for y in x['instances']:
                    print('['+str(counter)+'] '+y)
                    counter += 1
        #print(contents[self.pattern]['instances'])
        file.close()

    def pick_agent(self):
        self.i = input("option:")
        file = open("useragents.json", "r")
        contents = json.load(file, encoding='utf-8')
        counter = 0
        for x in contents:
            #for y in x['pattern']:
            #    print(y)
            #print(self.pattern)
            if x['pattern'] == self.pattern:
                for y in x['instances']:
                    if counter == int(self.i):
                        self.agent = y
                    
                    counter += 1
        #print(contents[self.pattern]['instances'])
        file.close()
        