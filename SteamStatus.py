from requests_html import HTMLSession
import time

profile_link = input ("Input a Steam profile link: ")

def getProfile(url):
    session = HTMLSession()
    r = session.get(url)
    r.html.render

    profile = {
        'Name': r.html.xpath('/html/body/div[1]/div[7]/div[6]/div/div[2]/div/div/div/div[1]/div[1]/span[1]', first = True).text,
        'Status': r.html.xpath('/html/body/div[1]/div[7]/div[6]/div/div[3]/div/div[1]/div[1]/div[1]/div', first = True).text,
    }
    print(profile.get("Name"))
    print(profile.get("Status"))
    if profile.get("Status") == 'Currently In-Game':
        profile["Game"] == r.html.xpath('/html/body/div[1]/div[7]/div[6]/div[1]/div[3]/div/div[1]/div[1]/div[1]/div[2]', first = True).text
        print(profile.get("Game"))
    return profile


getProfile(profile_link)