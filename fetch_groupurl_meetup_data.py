import requests
import json
import time

def main():
        a=[]
        cities =[("New York","NY")]
        api_key= "enter here"
        # Get your key here https://secure.meetup.com/meetup_api/key/
        for (city, state) in cities:
            per_page = 200
            results_we_got = per_page
            offset = 0
            while (results_we_got == per_page):
                # Meetup.com documentation here: http://www.meetup.com/meetup_api/docs/2/groups/
                response=get_results({"sign":"true","country":"US", "city":city, "state":state, "radius": 10, "key":api_key, "page":per_page, "offset":offset })
                time.sleep(1)
                offset += 1
                results_we_got = response['meta']['count']
                for group in response['results']:
                    try:
                        a.append([group['id'], group['link']])
                    except:
                        a.append([group['id'],[None]])
                    #print(a)
        with open('groupurl.json', 'w') as outfile:
            json.dump(a, outfile)
            time.sleep(1)


def get_results(params):

    request = requests.get("http://api.meetup.com/2/groups",params=params)
    data = request.json()

    return data


if __name__=="__main__":
        main()


## Run this script and send it into a json
