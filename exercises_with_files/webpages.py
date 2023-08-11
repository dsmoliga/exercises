import requests
from requests.adapters import HTTPAdapter

 
def read_websites(file_name):
    with open(file_name, "r", encoding="UTF=8") as file:
        websites = file.readlines()
        websites = [line.replace("\n", "") for line in websites]
        return websites
 
def check_websites(website):
    try:    
        s = requests.Session()
        s.mount("http://", HTTPAdapter(max_retries = 3))
        response = s.get(website, timeout = 1)
        if response.status_code == 200:
            return True
        else:
            return False
    except:
        return False
 
def filter_working_websites(websites):
    working_websites = []
    for website in websites:
        if check_websites(website):
            working_websites.append(website)
    return working_websites

def filter_not_working_websites(websites):
    not_working_websites = []
    for website in websites:
        if check_websites(website) == False:
            not_working_websites.append(website)
    return not_working_websites
        

def save_working_websites(working_websites, file_name):
    with open(file_name, "w", encoding="UTF=8") as file:
        for website in working_websites:
            file.write(website + "\n")

def save_not_working_websites(not_working_websites, file_name):
    with open(file_name, "w", encoding="UTF=8") as file:
        for website in not_working_websites:
            file.write(website + "\n")



websites = read_websites("websites.txt")

working_websites = filter_working_websites(websites)
save_working_websites(working_websites, "working_websites.txt")

not_working_websites = filter_not_working_websites(websites)
save_not_working_websites(not_working_websites, "not_working_websites.txt")