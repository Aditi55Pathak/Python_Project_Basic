import requests
import json
import win32com.client as wincl

query = input("What type of news are you intrestd in :- ")
url = f"https://newsapi.org/v2/everything?q={query}&apiKey=42301c39fa3142ffa29c7218d7959322"
r = requests.get(url)
news = json.loads(r.text)
# print(news,type(news))
for article in news["articles"]:
    print(article["title"])
    print(article["description"])
    print("*********************************")

print("Do you want to hear news? (Y & N)")
ans = input()
if ans.lower() == "y":
    speaker_number = 1
    spk = wincl.Dispatch("SAPI.SpVoice")
    vcs = spk.GetVoices()
    SVSFlag = 11
    print(vcs.Item(speaker_number).GetAttribute("Name"))  # speaker name
    spk.Voice
    spk.SetVoice(
        vcs.Item(speaker_number)
    )  # set voice (see Windows Text-to-Speech settings)
    spk.Speak(article)
else:
    print("Its ok!!!!")
