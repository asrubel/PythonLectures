import requests
from bs4 import BeautifulSoup

url = "https://realpython.github.io/fake-jobs/"
page = requests.get(url)

# print(page.text)

soup = BeautifulSoup(page.content, "html.parser")

res = soup.find_all("div", class_="card")
for el in res:
    # print(el, end="\n"*3)
    title_el = el.find("h2", class_="title")
    company_el = el.find("h3", class_="company")
    location_el = el.find("p", class_="location")
    print(title_el.text)
    print(company_el.text)
    print(location_el.text.strip(), end="\n" * 2)

python_jobs = soup.find_all("h2", string="Python")
print(python_jobs)

python_jobs = soup.find_all(
    "h2", string=lambda text: "python" in text.lower()
)
print(python_jobs)

python_job_elements = [el.parent.parent.parent for el in python_jobs]
print(python_job_elements)

for job_el in python_job_elements:
    links = job_el.find_all("a")
    for link in links:
        print(link.text.strip(), link["href"])

big_el = soup.find(id="ResultsContainer")
print(big_el.prettify())
