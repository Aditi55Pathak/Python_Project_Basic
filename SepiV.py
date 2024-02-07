import win32com.client as wincom

a = [
    "Mrinal loves Ishita",
    "Harshil loves Ayushi",
    "Varun Loves Aarya",
    "Sakshi loves Dhruvraj",
]

b = [
    "Kudiyon ka nasha payare nasha sabse nashila hai jise dekhu yahan vo husan ki barish mai gila hai ishq ke naam pe karte sabhi ab raas leela hai mai karu to saala character dheela hai ho mai karu to saala character dheela hai"
]
c="""You look at the world through your own eyes. A simple looking sentence that reflects so much power and so much regret! 
It's like being born with a million different blindnesses. A different kind of FOMO. I will always keep viewing this world from my eyes, which are habituated with a certain perspective, they're decorated but at the same time tainted with my experiences. I wonder if i'll ever be able to look at a sunrise and see the same orange and yellow hazes as someone sitting beside me watching the same sunset.
Its a boon to have a perspective, but its also a curse sometimes, a curse that will never let me see what someone else is able to. I can try and understand their varying perspectives maybe, but only understand, never can i ever see it in its full real form. Is that why reality is so warped? Maybe, maybe not.
Maybe we all see the things in a similar tone, maybe we just make out different philosophies out of it. Whatever it maybe, we are all blind and always will be...starved of the views of the billions of others around.
"""
speak = wincom.Dispatch("SAPI.SpVoice")
text = "Python text-to-speech test. using win32com.client"
# speak.Speak(a)
# speak.Speak(b)
speak.Speak(c)

import win32com.client as wincl

a = [
    "Darde dil ke bina mehefil he kya aaa... Jo na tuta vo kabhi dil he kyaa.. Hai mera haal bura aur bura kardiya mere zhakhamo ko aur bura kardiya oooo bedardiya pyaar bedardiya"
]

speaker_number = 1
spk = wincl.Dispatch("SAPI.SpVoice")
vcs = spk.GetVoices()
SVSFlag = 11
print(vcs.Item(speaker_number).GetAttribute("Name"))  # speaker name
spk.Voice
spk.SetVoice(
    vcs.Item(speaker_number)
)  # set voice (see Windows Text-to-Speech settings)
# spk.Speak(a)

# Start by importing the win32com package
