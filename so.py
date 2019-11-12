import requests
from bs4 import BeautifulSoup

URL = f"https://stackoverflow.com/jobs?q=python&sort=i"


def get_last_page():
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, "html.parser")
    pages = soup.find("div", {"class": "pagination"}).find_all("a")
    return pages

# def extract_jobs(last_page):


def get_jobs():
    last_page = get_last_page()
    # jobs = extract_jobs(last_page)
    return last_page
