import requests
import json
from requests.structures import CaseInsensitiveDict

def api_service():


    limit = int(input('Enter limit value :'))
    offset = int(input('Enter offset value :'))
    artist_id = input('Enter artist id :')
    #'65f4f0c5-ef9e-490c-aee3-909e7ae6b2ab'

    url = f'http://musicbrainz.org/ws/2/release-group?artist={artist_id}&offset={offset}&limit={limit}'

    headers = CaseInsensitiveDict()
    headers["Accept"] = "application/json"
    response = requests.get( url, headers=headers) 


    '''The service returns a list of release-groups of type Album and the number of releases in each
    release-group. (A release is something you can buy as media, such as a CD or a vinyl
    record, while a release group embraces the overall concept of an album).

                Here is the JSON result you need to produce:
                {
                "albums":[
                            {
                                "id":"65f4f0c5-ef9e-490c-aee3-909e7ae6b2ab",
                                "title":"Ride the Lightning",
                                "year":1984,
                                "release_count":5
                            },
                            {
                                "id":"3d00fb45-f8ab-3436-a8e1-b4bfc4d66913",
                                "title":"Master of Puppets",
                                "year":1986,
                                "release_count":47
                            }
                ]
                }
    '''

    release_groups_json = json.loads(response.text)
    #for _ in range(limit):
    album_list = []
    for i in range(limit):
        service_ = {
            "id": release_groups_json['release-groups'][i]['id'],
            "title": release_groups_json['release-groups'][i]['title'],
            "year": release_groups_json['release-groups'][i]['first-release-date'],
            "release_count": release_groups_json['release-group-count'],
            #or 0,
        }
        album_list.append(service_)
    print({"albums":album_list})

api_service()


