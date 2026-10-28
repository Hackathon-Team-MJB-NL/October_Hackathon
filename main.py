from google import genai
from dotenv import load_dotenv
import os
import requests
from bs4 import BeautifulSoup
from ui import UI

load_dotenv()
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')



def get_url():
    name1, number1, name2, number2 = UI()
    url1 = (
        "https://www.swimmingresults.org/individualbest/"
        f"personal_best.php?back=individualbestname&mode=A&name={name1}&tiref={number1}"
    )
    url2 = (
        "https://www.swimmingresults.org/individualbest/"
        f"personal_best.php?back=individualbestname&mode=A&name={name2}&tiref={number2}"
    )
    return url1, url2

def get_data():
    url1 = get_url()[0]
    url2 = get_url()[1]
    urls = [url1, url2]
    times = []
    for i in urls:
        headers = {
            "User-Agent": "Mozilla/5.0"
            }
        
        response = requests.get(i, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        tables = soup.find_all("table")
        print(f"Found {len(tables)} tables")

        lc_table = tables[0]

        rows = lc_table.find_all("tr")

        for row in rows:
            cells = row.find_all(["td", "th"])
            print([cell.get_text(strip=True) for cell in cells])
        times.append([cell.get_text(strip=True) for cell in cells])
    return times



lc_table = get_data()
client = genai.Client(api_key=GEMINI_API_KEY)
#loughboguh training schedule 
nm_training_in_pool = 8
nm_training_in_gym = 3
print("""
      
      
      
      
      
      
      
      
      
      
      
      """)
response = client.models.generate_content(
    model="gemma-4-26b-a4b-it",
    contents=f"""SWIMMER 1:{lc_table[0]}, using this training schedule {nm_training_in_pool} training in the pool and {nm_training_in_gym} training in the gym. Using the training schedule and data given predict the swimmers times in one year in a table without any other information.
            SWIMMER 2:{lc_table[1]}, using this training schedule {nm_training_in_pool} training in the pool and {nm_training_in_gym} training in the gym. Using the training schedule and data given predict the swimmers times in one year in a table without any other information. Do a quick summary of who will be better in a year in an event they are both pretty good at""",
)
print(response.text)
