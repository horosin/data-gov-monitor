import requests
import json


def get_mock_data(data_point_number = 100):

    dane_gov_request_url = f'https://api.dane.gov.pl/datasets?page=1&per_page={data_point_number}&sort=-verified'

    response = requests.get(dane_gov_request_url)
    content_dict = json.loads(response.content)

    uris_with_metadata = []

    for api_endpoint in content_dict['data']:
        attributes = api_endpoint['attributes']
        title = attributes['title']
        if 'title' in attributes['category'].keys():
            category_name = attributes['category']['title']
            category_id = attributes['category']['id']
        else:
            category_name = ''
            category_id = ''
        uri = api_endpoint['links']['self']
        uris_with_metadata.append((uri, title, category_name, category_id))

    return uris_with_metadata
