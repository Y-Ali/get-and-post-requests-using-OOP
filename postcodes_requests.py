import requests # library for making http requests
import json

class PostcodesConnection:

    def __init__(self):
        self.parameter = ''
        self.path = 'https://api.postcodes.io/postcodes/'
        self.result = ''
        self. status = ''

    def look_up_one_postcode(self, post_code):
        connection = requests.get(self.path + post_code)    # creating the connection with the API using the path and the parameter-(the postcode)
        #print(connection)

        dictionary_of_connection = connection.json()        # creating the json (a hash) of all the data (postcodes)
        print(type(dictionary_of_connection))

        status = dictionary_of_connection['status']         # status key
        results = dictionary_of_connection['result']        # the result key

        self.result = results
        self.status = status

        #print(self.result)

        for item in self.result.keys():
            print(item, ":", self.result[item])


    def output_region_country(self):

        print(self.result.keys())
        print(self.result['country'])
        print(self.result['region'])


    def output_lat_long(self):
        print(self.result['latitude'])
        print(self.result['longitude'])

    def output_all_details(self):

        for key in self.result:
            print(key, ":", self.result[key])

    def output_one_value(self):
        print("")

    def post_requestsssss(self,post_code):
        self.post_code = post_code
        self.path = 'https://api.postcodes.io/postcodes/'

        self.post_request_to_postcodes = ''
        self.json_body = json.dumps({"postcodes": self.post_code})
        self.headers = {'Content-Type': 'application/json'}

        print(self.json_body)

        self.post_request_postcodes = requests.post(self.path, headers=self.headers, data=self.json_body)


