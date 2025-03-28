import requests
from bs4 import BeautifulSoup

http_text = requests.get("https://weather.com/en-CA/weather/tenday/l/aba7999ac37e8e853eb550dd46f1263cd14f6ea93d9acc5978bae9e1219f9fde#detailIndex5").text
soup = BeautifulSoup(http_text, 'lxml')

weather_data = soup.find_all('div', class_="DetailsSummary--DetailsSummary--Mt7BE DetailsSummary--fadeOnOpen--VFqHQ DetailsSummary--dailyDetailsSummary--AErKu")

with open('ELEC292_Lab2.txt', 'a') as f:
    for day in weather_data:
        date = day.find('h2', class_ = "DetailsSummary--daypartName--CcVUz").text
        temp_section = day.find('div', class_="DetailsSummary--temperature--YGmQ5")
        max_temp = temp_section.find('span', class_="DetailsSummary--highTempValue--VHKaO").text
        min_temp = temp_section.find('span', class_="DetailsSummary--lowTempValue--ogrzb").text
        weather_condition = day.find('div', class_="DetailsSummary--condition--OHCn3").span.text
        chance = day.find('div', class_="DetailsSummary--precip--YXw9t").span.text
        wind_section = day.find('div', class_="DetailsSummary--wind--8txPR DetailsSummary--extendedData--eJzhb")
        direction_speed = wind_section('span', class_="Wind--windWrapper--NsCjc undefined")

        direction_speed = direction_speed[0].find_all('span')
        direction = direction_speed[0].text
        speed = direction_speed[1].text

        final_data = (date, max_temp, min_temp, weather_condition, chance, direction,speed)

        print(final_data, file=f)


