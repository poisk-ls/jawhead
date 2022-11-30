#! /usr/bin/python3
from requests import get,exceptions
from os import system
from argparse import ArgumentParser
from json import dump
parser = ArgumentParser()
parser.add_argument("username",nargs='*',help='- pass the username , example:  $aliens_eye aaron123')
args = parser.parse_args()
r = "\033[31m"
g = "\033[32m"
y = "\033[33m"
b='\33[36m'
p = "\033[35m"
banner=f"""{y}

 ───█ █▀▀█ █───█
─▄─ █ █▄▄█ █▄█▄█
 █▄▄█ ▀──▀ ─▀─▀─
{r}
   
    █──█ █▀▀ █▀▀█ █▀▀▄
    █▀▀█ █▀▀ █▄▄█ █──█
    ▀──▀ ▀▀▀ ▀──▀ ▀▀▀
      
{g}code: {y}poisk-ls
{g}github:{r}poisk-ls
"""
def scanner(u):
 save_json={}
 social={
 "Facebook":f"https://facebook.com/{u}",
 "Messenger":f"https://m.me/{u}",
 "Youtube":f"https://youtube.com/{u}",
 "Instagram":f"https://instagram.com/{u}",
 "Vimeo":f"https://vimeo.com/{u}",
 "Github":f"https://github.com/{u}",
 "Plus":f"https://plus.google.com/{u}",
 "Pinterest":f"https://pinterest.com/{u}",
 "Flickr":f"https://flickr.com/people/{u}",
 "Vk":f"https://vk.com/{u}",
 "About":f"https://about.me/{u}",
 "Disqus":f"https://disqus.com/{u}",
 "Bitbucket":f"https://bitbucket.org/{u}",
 "Flipboard":f"https://flipboard.com/@{u}",
 "Twitter":f"https://twitter.com/{u}",
 "Medium":f"https://medium.com/@{u}",
 "Hackerone":f"https://hackerone.com/{u}",
 "Keybase":f"https://keybase.io/{u}",
 "Buzzfeed":f"https://buzzfeed.com/{u}",
 "Slideshare":f"https://slideshare.net/{u}",
 "Mixcloud":f"https://mixcloud.com/{u}",
 "Soundcloud":f"https://soundcloud.com/{u}",
 "Badoo":f"https://badoo.com/en/{u}",
 "Imgur":f"https://imgur.com/user/{u}",
 "Spotify":f"https://open.spotify.com/user/{u}",
 "Pastebin":f"https://pastebin.com/u/{u}",
 "Wattpad":f"https://wattpad.com/user/{u}",
 "Canva":f"https://canva.com/{u}",
 "Codecademy":f"https://codecademy.com/{u}",
 "Last":f"https://last.fm/user/{u}",
 "Blip":f"https://blip.fm/{u}",
 "Dribbble":f"https://dribbble.com/{u}",
 "Gravatar":f"https://en.gravatar.com/{u}",
 "Foursquare":f"https://foursquare.com/{u}",
 "Creativemarket":f"https://creativemarket.com/{u}",
 "Ello":f"https://ello.co/{u}",
 "Cash":f"https://cash.me/{u}",
 "Angel":f"https://angel.co/{u}",
 "Wikipedia":f"https://www.wikipedia.org/wiki/User:{u}",
 "500px":f"https://500px.com/{u}",
 "Houzz":f"https://houzz.com/user/{u}",
 "Tripadvisor":f"https://tripadvisor.com/members/{u}",
 "Kongregate":f"https://kongregate.com/accounts/{u}",
 "blogspot":f"https://{u}.blogspot.com/",
 "tumblr":f"https://{u}.tumblr.com/",
 "Wordpress":f"https://{u}.wordpress.com/",
 "Devianart":f"https://{u}.devianart.com/",
 "Designspiration":f"https://www.designspiration.net/{u}",
 "Slack":f"https://{u}.slack.com/",
 "Livejournal":f"https://{u}.livejournal.com/",
 "Newgrounds":f"https://{u}.newgrounds.com/",
 "Hubpages":f"https://{u}.hubpages.com",
 "Contently":f"https://{u}.contently.com",
 "Steamcommunity":f"https://steamcommunity.com/id/{u}",
 "Freelancer":f"https://www.freelancer.com/u/{u}",
 "Dailymotion":f"https://www.dailymotion.com/{u}",
 "Instructables":f"https://www.instructables.com/member/{u}",
 "Etsy":f"https://www.etsy.com/shop/{u}",
 "Scribd":f"https://www.scribd.com/{u}",
 "Colourlovers":f"https://www.colourlovers.com/love/{u}",
 "Patreon":f"https://www.patreon.com/{u}",
 "Behance":f"https://www.behance.net/{u}",
 "Goodreads":f"https://www.goodreads.com/{u}",
 "Gumroad":f"https://www.gumroad.com/{u}",
 "Codementor":f"https://www.codementor.io/{u}",
 "Reverbnation":f"https://www.reverbnation.com/{u}",
 "Bandcamp":f"https://www.bandcamp.com/{u}",
 "Ifttt":f"https://www.ifttt.com/p/{u}",
 "Trakt":f"https://www.trakt.tv/users/{u}",
 "Okcupid":f"https://www.okcupid.com/profile/{u}",
 "Trip":f"https://www.trip.skyscanner.com/user/{u}",
 "Zone-h":f"http://www.zone-h.org/archive/notifier={u}"
 }
 print(f"\n{y}Fetching details of {u}:\n")
 spece=" "*20
 print(f"{g}#"*126)
 print(f"{g}# {r}SOCIAL MEDIA   {g}|        {r}USER {g}        | {r}STATUS CODE{g} | {r}                   URL   {g}      {spece}                   #")
 for i,j in social.items():
  try:
   req = get(j)
   code=req.status_code
  except exceptions.TooManyRedirects:
   print("TooManyRedirects")
   break
  except exceptions.ConnectionError:
   print("\n\nConnectionError!\n\ncheck your internet connection!\n\n")
   break
  except exceptions.Timeout: 
   continue
  print(f"{g}#"+f"{p}-"*124+f"{g}#")
  if code==200:
   user1="Found"
   user=f"{g}|{y}        Found        "
  elif code==404:
   user1="Not Found"
   user=f"{g}|{r}      Not Found      "
  else:
   user1="undefined status code"
   user=f"{g}|{b}undefined status code"
   j="none"
  save_json[i]={"code:":code,"user:":user1,"url:":j}
  media=f"{g}# {y}"+i+" "*(15-len(i))
  code=f"{g}|     {y}"+str(code)+" "*5
  url=f"{g}|{y} "+j+" "*(70-len(j))+f"{g}#"
  print(media+user+code+url)
  with open(u+".json","w") as f:
   dump(save_json,f,indent=4)
 print("#"*126)
 print(f"\n{y}Data has been saved in {u}.json")
def main(usernames):
 system("clear")
 print(banner)
 print(f"{r}NOTE:The data may not be completely accurate!\n")
 print(f"{r}NOTE: for educational purpose only!\n")
 if usernames == []:
  usernames=input(f"{y}Enter the username{r}:{g}").split()
 for username in usernames:
    scanner(username)
 print(f"\n{r}vist {g}https://en.wikipedia.org/wiki/List_of_HTTP_status_codes{r} to know more about status codes!\n")
 print(f"{b}Thank you\n")
if __name__ == "__main__":
 main(args.username)
