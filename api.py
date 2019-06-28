# from secrets import PET_FINDER_API_KEY, SECRET_PET_FINDER_API_KEY
import requests

token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6ImUwMTYwZDA3MTVhOGM4MGFmNzgwY2Y5ZWMxYzg5YjI1MzhhYzc5NmJmYzNlNTFjZDc2NzdlMGIzNjNlOTRlMmE2NzZhOTU5NTExOWQ2NWRiIn0.eyJhdWQiOiJaaWFGR1Rra3pFVlc1SmFadWRiZ1BxMXJZeWVJeTd0VlZDM05BdmtMZ2djUTFWanZDMiIsImp0aSI6ImUwMTYwZDA3MTVhOGM4MGFmNzgwY2Y5ZWMxYzg5YjI1MzhhYzc5NmJmYzNlNTFjZDc2NzdlMGIzNjNlOTRlMmE2NzZhOTU5NTExOWQ2NWRiIiwiaWF0IjoxNTYxNzY0NTkwLCJuYmYiOjE1NjE3NjQ1OTAsImV4cCI6MTU2MTc2ODE5MCwic3ViIjoiIiwic2NvcGVzIjpbXX0.JZtMcn5KGYbjED3Ni5CkHNXHnTTynRf6qW32wCHoxqrclNK-OZDTikNSZAkrpTxQQJbLRpONj55dD4nFSKwBN2Pc-_2C8veyz5eAYVdAMcmcDnL8-cMP0rdqdTZOeAcHnf5UZWIxrL-kOjCd8w1HeqeU0-0eem2Jc-YRShVuvS-beGX_8-L7puL0Yv4jiSxnt5z1FTXm3Rt862CWLrq2m2urFnc1PHNa0DwJdNuI_3Ikd-oGfUvrzEhZMnz8YPctw3TjpMpL5ERVma0J4mjZ77Bs_ph-2EM2jAVdZ5ct7pGfaltWmTMqe14KorhGTTqgMQm7ezmXiFPrNFKft2sY9A'

PLACEHOLDER_PHOTO = "https://bit.ly/31YSHxD"

# def get_token():
#     """ Get a token to access the pet finder API """
#     data = {
#         'grant_type': 'client_credentials',
#         'client_id': PET_FINDER_API_KEY,
#         'client_secret': SECRET_PET_FINDER_API_KEY
#     }

#     raw_resp = requests.post('https://api.petfinder.com/v2/oauth2/token', data=data)
#     resp = raw_resp.json()
#     token = resp['access_token']

#     return token


def get_pet_info():
    """ Get a random pet listing from the pet finder api
    Return a dictionary containing the pets' name, species, age, and photo URL """

    # Get a token
    # token = get_token()

    raw_resp = requests.get("https://api.petfinder.com/v2/animals",
        headers={"Authorization":f"Bearer {token}"})

    resp = raw_resp.json()

    # if entry does not have a photo, use the default photo
    photo_url = resp['animals'][0]['photos'][0]['medium'] if (resp['animals'][0]['photos']) else PLACEHOLDER_PHOTO
    name = resp['animals'][0]['name']
    species = resp['animals'][0]['species']
    age = resp['animals'][0]['age']

    print(resp['animals'][0]['photos'])
    pet_info_dictionary = dict([('name', name), ('species', species), ('age', age), ('photo_url', photo_url)])

    return pet_info_dictionary

