import urllib
import re
from bs4 import BeautifulSoup
import streamlit as st
from PIL import Image
from playsound import playsound
import time

st.set_page_config(page_title="My Website", page_icon=":tada", layout="wide")
i=0
x1=10000
y1=10000
a1=10000
b1=10000
c1=10000
d1=10000
e1=10000
f1=10000
while i == 0:
#Sensor 1 Temperature 
 datafromwebsite=urllib.request.urlopen("https://api.thingspeak.com/channels/1708546/fields/1.json?results=1");
 select=repr(datafromwebsite.read());
 select=select[::-1]
 pick=re.search('}]}(.+?):"1dleif',select)
 m=repr(pick);
 m=m[::-1]
 fannie=re.search('field1":"(.+?)"',m)
 if fannie:
   print(fannie.group(1));
 x= float(fannie.group(1))
 print(x)
 if x1 != x:
  if x > 24:
   st.subheader("Sensor 1")
   st.write("Sensor 1 Temperature is")
   st.write(x)
   telegramtemp1=urllib.request.urlopen("https://api.telegram.org/bot5577403616:AAEB5Ix0BQuSEeLRn8sCcc2nkdk8xCfsGIc/sendMessage?chat_id=@group6dfc&text=Sensor%201%20has%20detected%20temperatures%20above%2024%20.%20Stay%20alert")
   st.write("[Threshold Reached>](https://217053524.wixsite.com/my-site-1")
  elif x < 15:
   st.subheader("Sensor 1")
   st.write("Sensor 1 Temperature is")
   st.write(x)
   telegramtemp1=urllib.request.urlopen("https://api.telegram.org/bot5577403616:AAEB5Ix0BQuSEeLRn8sCcc2nkdk8xCfsGIc/sendMessage?chat_id=@group6dfc&text=Sensor%201%20has%20detected%20temperatures%20below%2015%20.%20Stay%20alert")
   st.write("[Threshold Reached>](https://217053524.wixsite.com/my-site-2)")  
  else:
   st.subheader("Sensor 1")
   st.write("Sensor 1 Temperature is")
   st.write(x)
 x1=x 
#Sensor 1 Humidity
 datafromwebsite=urllib.request.urlopen(" https://api.thingspeak.com/channels/1708546/fields/2.json?results=1");
 select=repr(datafromwebsite.read());
 select=select[::-1]
 pick=re.search('}]}(.+?):"2dleif',select)
 m=repr(pick);
 m=m[::-1]
 fannie=re.search('field2":"(.+?)"',m)
 if fannie:
   print(fannie.group(1));
   x = float(fannie.group(1))
 print(x)
 if y1 != x:
  if x > 50:
   st.subheader("Sensor 1")
   st.write("Sensor 1 humidity is")
   st.write(x)
   telegramhum1=urllib.request.urlopen("https://api.telegram.org/bot5577403616:AAEB5Ix0BQuSEeLRn8sCcc2nkdk8xCfsGIc/sendMessage?chat_id=@group6dfc&text=Sensor%201%20has%20detected%20humidity%20above%2050%%20.%20Stay%20alert")
   st.write("[Threshold Reached>](https://dungasinovuyo6.wixsite.com/my-site-2)")  
  elif x < 0:
   st.subheader("Sensor 1")
   st.write("Sensor 1 humidity is")
   st.write(x)
   telegramhum1=urllib.request.urlopen("https://api.telegram.org/bot5577403616:AAEB5Ix0BQuSEeLRn8sCcc2nkdk8xCfsGIc/sendMessage?chat_id=@group6dfc&text=Sensor%201%20has%20detected%20humidity%20below%200%%20.%20Stay%20alert")
   st.write("[Threshold Reached>](https://dungasinovuyo6.wixsite.com/my-site-1)") 
  else:
   st.subheader("Sensor 1")
   st.write("Sensor 1 humidity is")
   st.write(x)
 y1=x
#Sensor 1 Temperature 
 datafromwebsite=urllib.request.urlopen(" https://api.thingspeak.com/channels/1737929/fields/1.json?results=1");
 select=repr(datafromwebsite.read());
 select=select[::-1]
 pick=re.search('}]}(.+?):"1dleif',select)
 m=repr(pick);
 m=m[::-1]
 fannie=re.search('field1":"(.+?)"',m)
 if fannie:
   print(fannie.group(1));
 x= float(fannie.group(1))
 print(x)
 if a1 != x:
  if x > 24:
   st.subheader("Sensor 2")
   st.write("Sensor 2 temperature is")
   st.write(x)
   telegramtemp1=urllib.request.urlopen("https://api.telegram.org/bot5577403616:AAEB5Ix0BQuSEeLRn8sCcc2nkdk8xCfsGIc/sendMessage?chat_id=@group6dfc&text=Sensor%202%20has%20detected%20temperatures%20above%2024%20.%20Stay%20alert")
   st.write("[Threshold Reached>](https://217053524.wixsite.com/my-site-3)")
  elif x < 15:
   st.subheader("Sensor 2")
   st.write("Sensor 2 temperature is")
   st.write(x)
   telegramtemp1=urllib.request.urlopen("https://api.telegram.org/bot5577403616:AAEB5Ix0BQuSEeLRn8sCcc2nkdk8xCfsGIc/sendMessage?chat_id=@group6dfc&text=Sensor%202%20has%20detected%20temperatures%20below%2015%20.%20Stay%20alert")
   st.write("[Threshold Reached>](https://217053524.wixsite.com/my-site-4)")  
  else:
   st.subheader("Sensor 2")
   st.write("Sensor 2 temperature is")
   st.write(x)
 a1=x 
#Sensor 1 Humidity
 datafromwebsite=urllib.request.urlopen(" https://api.thingspeak.com/channels/1737929/fields/2.json?results=1");
 select=repr(datafromwebsite.read());
 select=select[::-1]
 pick=re.search('}]}(.+?):"2dleif',select)
 m=repr(pick);
 m=m[::-1]
 fannie=re.search('field2":"(.+?)"',m)
 if fannie:
   print(fannie.group(1));
   x = float(fannie.group(1))
 print(x)
 if b1 != x:
  if x > 50:
   st.subheader("Sensor 2")
   st.write("Sensor 2 humidity is")
   st.write(x)
   telegramhum1=urllib.request.urlopen("https://api.telegram.org/bot5577403616:AAEB5Ix0BQuSEeLRn8sCcc2nkdk8xCfsGIc/sendMessage?chat_id=@group6dfc&text=Sensor%202%20has%20detected%20humidity%20above%2050%%20.%20Stay%20alert")
   st.write("[Threshold Reached>](https://dungasinovuyo6.wixsite.com/my-site-4)")  
  elif x < 0:
   st.subheader("Sensor 2")
   st.write("Sensor 2 humidity is")
   st.write(x)
   telegramhum1=urllib.request.urlopen("https://api.telegram.org/bot5577403616:AAEB5Ix0BQuSEeLRn8sCcc2nkdk8xCfsGIc/sendMessage?chat_id=@group6dfc&text=Sensor%202%20has%20detected%20humidity%20below%200%%20.%20Stay%20alert")
   st.write("[Threshold Reached>](https://dungasinovuyo6.wixsite.com/my-site-3)") 
  else:
   st.subheader("Sensor 2")
   st.write("Sensor 2 humidity is")
   st.write(x)
  b1=x
 #Sensor 1 Temperature 
 datafromwebsite=urllib.request.urlopen(" https://api.thingspeak.com/channels/1738066/fields/1.json?results=1");
 select=repr(datafromwebsite.read());
 select=select[::-1]
 pick=re.search('}]}(.+?):"1dleif',select)
 m=repr(pick);
 m=m[::-1]
 fannie=re.search('field1":"(.+?)"',m)
 if fannie:
   print(fannie.group(1));
 x= float(fannie.group(1))
 print(x)
 if c1 != x:
  if x > 24:
   st.subheader("Sensor 3")
   st.write("Sensor 3 temperature is")
   st.write(x)
   telegramtemp1=urllib.request.urlopen("https://api.telegram.org/bot5577403616:AAEB5Ix0BQuSEeLRn8sCcc2nkdk8xCfsGIc/sendMessage?chat_id=@group6dfc&text=Sensor%203%20has%20detected%20temperatures%20above%2024%20.%20Stay%20alert")
   st.write("[Threshold Reached>](https://217053524.wixsite.com/my-site-5)")
  elif x < 15:
   st.subheader("Sensor 3")
   st.write("Sensor 3 temperature is")
   st.write(x)
   telegramtemp1=urllib.request.urlopen("https://api.telegram.org/bot5577403616:AAEB5Ix0BQuSEeLRn8sCcc2nkdk8xCfsGIc/sendMessage?chat_id=@group6dfc&text=Sensor%203%20has%20detected%20temperatures%20below%2015%20.%20Stay%20alert")
   st.write("[Threshold Reached>](https://217053524.wixsite.com/my-site-6)")  
  else:
   st.subheader("Sensor 3")
   st.write("Sensor 3 temperature is")
   st.write(x)
 c1=x 
#Sensor 1 Humidity
 datafromwebsite=urllib.request.urlopen(" https://api.thingspeak.com/channels/1738066/fields/2.json?results=1");
 select=repr(datafromwebsite.read());
 select=select[::-1]
 pick=re.search('}]}(.+?):"2dleif',select)
 m=repr(pick);
 m=m[::-1]
 fannie=re.search('field2":"(.+?)"',m)
 if fannie:
   print(fannie.group(1));
   x = float(fannie.group(1))
 print(x)
 if d1 != x:
  if x > 50:
   st.subheader("Sensor 3")
   st.write("Sensor 3 humidity is")
   st.write(x)
   telegramhum1=urllib.request.urlopen("https://api.telegram.org/bot5577403616:AAEB5Ix0BQuSEeLRn8sCcc2nkdk8xCfsGIc/sendMessage?chat_id=@group6dfc&text=Sensor%203%20has%20detected%20humidity%20above%2050%%20.%20Stay%20alert")
   st.write("[Threshold Reached>](https://217053524.wixsite.com/my-site-6)")  
  elif x < 0:
   st.subheader("Sensor 3")
   st.write("Sensor 3 humidity is")
   st.write(x)
   telegramhum1=urllib.request.urlopen("https://api.telegram.org/bot5577403616:AAEB5Ix0BQuSEeLRn8sCcc2nkdk8xCfsGIc/sendMessage?chat_id=@group6dfc&text=Sensor%203%20has%20detected%20humidity%20below%200%%20.%20Stay%20alert")
   st.write("[Threshold Reached>](https://217053524.wixsite.com/my-site-5)") 
  else:
   st.subheader("Sensor 3")
   st.write("Sensor 3 humidity is")
   st.write(x)
 d1=x
 #Sensor 1 Temperature 
 datafromwebsite=urllib.request.urlopen(" https://api.thingspeak.com/channels/1738082/fields/1.json?results=1");
 select=repr(datafromwebsite.read());
 select=select[::-1]
 pick=re.search('}]}(.+?):"1dleif',select)
 m=repr(pick);
 m=m[::-1]
 fannie=re.search('field1":"(.+?)"',m)
 if fannie:
   print(fannie.group(1));
 x= float(fannie.group(1))
 print(x)
 if e1 != x:
  if x > 24:
   st.subheader("Sensor 4")
   st.write("Sensor 4 temperature is")
   st.write(x)
   telegramtemp1=urllib.request.urlopen("https://api.telegram.org/bot5577403616:AAEB5Ix0BQuSEeLRn8sCcc2nkdk8xCfsGIc/sendMessage?chat_id=@group6dfc&text=Sensor%204%20has%20detected%20temperatures%20above%2024%20.%20Stay%20alert")
   st.write("[Threshold Reached>](https://217053524.wixsite.com/my-site-7)")
  elif x < 15:
   st.subheader("Sensor 4")
   st.write("Sensor 4 temperature is")
   st.write(x)
   telegramtemp1=urllib.request.urlopen("https://api.telegram.org/bot5577403616:AAEB5Ix0BQuSEeLRn8sCcc2nkdk8xCfsGIc/sendMessage?chat_id=@group6dfc&text=Sensor%204%20has%20detected%20temperatures%20below%2015%20.%20Stay%20alert")
   st.write("[Threshold Reached>](https://217053524.wixsite.com/my-site-8)")  
  else:
   st.subheader("Sensor 4")
   st.write("Sensor 4 temperature is")
   st.write(x)
 e1=x 
#Sensor 1 Humidity
 datafromwebsite=urllib.request.urlopen("https://api.thingspeak.com/channels/1738082/fields/2.json?results=1");
 select=repr(datafromwebsite.read());
 select=select[::-1]
 pick=re.search('}]}(.+?):"2dleif',select)
 m=repr(pick);
 m=m[::-1]
 fannie=re.search('field2":"(.+?)"',m)
 if fannie:
   print(fannie.group(1));
   x = float(fannie.group(1))
 print(x)
 if f1 != x:
  if x > 50:
   st.subheader("Sensor 4")
   st.write("Sensor 4 humidity is")
   st.write(x)
   telegramhum1=urllib.request.urlopen("https://api.telegram.org/bot5577403616:AAEB5Ix0BQuSEeLRn8sCcc2nkdk8xCfsGIc/sendMessage?chat_id=@group6dfc&text=Sensor%204%20has%20detected%20humidity%20above%2050%%20.%20Stay%20alert")
   st.write("[Threshold Reached>](https://dungasinovuyo6.wixsite.com/my-site-8)") 
  elif x < 0:
   st.subheader("Sensor 4")
   st.write("Sensor 4 humidity is")
   st.write(x)
   telegramhum1=urllib.request.urlopen("https://api.telegram.org/bot5577403616:AAEB5Ix0BQuSEeLRn8sCcc2nkdk8xCfsGIc/sendMessage?chat_id=@group6dfc&text=Sensor%204%20has%20detected%20humidity%20below%200%%20.%20Stay%20alert")
   st.write("[Threshold Reached>](https://dungasinovuyo6.wixsite.com/my-site-7)") 
  else:
   st.subheader("Sensor 4")
   st.write("Sensor 4 humidity is")
   st.write(x)
 f1=x
 time.sleep(6)
i=0




