import requests
import json
import time
import pandas as pd

groupid = pd.read_json('groupid.json',typ='series')
#slice groupid if API time-out issues
groupid_seg = groupid.iloc[0:]

def main():
        a=[]
        api_key= "enter here"
        # Get your key here https://secure.meetup.com/meetup_api/key/
        for ID in groupid_seg:
            per_page = 200
            results_we_got = per_page
            offset = 0
            while (results_we_got == per_page):
                # Meetup.com documentation here: http://www.meetup.com/meetup_api/docs/2/events/
                response=get_results({"group_id": ID, "limited_events":"true", "status":"past", "time":"-36m,", "key":api_key, "page":per_page, "offset":offset })
                time.sleep(1)
                offset += 1
                results_we_got = response['meta']['count']
                #print len(response['results'][0][0])
                for event in response['results']:
                    try:
                        a.append([ID, event['time'],event['yes_rsvp_count']] )
                    except:
                        a.append([ID, event['time'],[None]])
                    #print(a)
        with open('eventtime_slice.json', 'w') as outfile:
            json.dump(a, outfile)
            time.sleep(1)


def get_results(params):

    request = requests.get("http://api.meetup.com/2/events",params=params)
    data = request.json()

    return data


if __name__=="__main__":
        main()

## Run this script and send it into a json
