import requests 
from bs4 import BeautifulSoup
import pandas 
oyo_url="https://www.trivago.in/en-IN/srl/hotels-badrinath-india?search=200-344788;dr-20220615-20220616;rc-5-11"
content=req.content
soup=BeautifulSoup(content,"html.parser")
all_hotels= soup.find_all("div",{"class":"bg-white rounded 2xl:rounded-sm SlideoutContainer_shadow__CA7DE"})
scraped_info_list=[]
for hotel in all_hotels:
  hotel_dict={}
  hotel_dict["name"]=hotel.find("span",{"itemprop":"name"}).text
  hotel_dict["location"]=hotel.find("span",{"class":"block text-s text-left text-s"}).text
  hotel_dict["price"]=hotel.find("p",{"itemprop":"price"}).text
  try:
    hotel_dict["ratings"]=hotel.find("span",{"itemprop":"ratingValue"}).text
  except AttributeError:
    pass
  ameneties_list=[]
  parent_element=hotel.find("div",{"class":"px-2 pb-2"})
  for flex space-x-1 pb-1 in parent_element.find_all("button",{"class":"flex space-x-1 pb-1"}):
   ameneties_list.append(flex space-x-1 pb-1.find("span",{"class":"flex items-center space-x-1 text-grey-900 text-s AccommodationInfo_part__rjilM"}).text.strip())
  hotel_dict["ammenities"]=','.join(ameneties_list[:-1])
  scraped_info_list.append(hotel_dict)

  print(hotel_name,hotel_location,hotel_price,hotel_ratings,ameneties_list)
dataFrame=pandas.DataFrame(scraped_info_list)
dataFrame.to_csv("trivago.csv")
