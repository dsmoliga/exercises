import requests
 
def read_websites(file_name):
    with open(file_name, "r", encoding="UTF=8") as file:
        websites_to_format = file.readlines()
        websites = []
        for line in websites_to_format:
            websites.append(line.replace("\n", ""))
        return websites
 
def check_websites(website):
    try:
        response = requests.get(website)
        if response.status_code == 200 :
            return True
        else :
            return False
    except:
        return False 
 
def filter_working_websites(websites):
    working_websites = []
    for website in websites:
        if check_websites(website):
            working_websites.append(website)
    return working_websites
        
def save_working_websites(working_websites, file_name):
    with open(file_name, "w", encoding="UTF=8") as file:
        for website in working_websites:
            file.write(website + "\n")
 
 
websites = read_websites("websites.txt")
working_websites = filter_working_websites(websites)
save_working_websites(working_websites, "working_websites.txt")