# libraries to read csv of links
import pandas
import os.path
import sys
import requests
import json

try:
    # Read file scraped today
    recent = pandas.read_csv('groupsLinks_daily.csv')
    print("number of links read today: ",len(recent))
    # Remove duplicate links from today's file
    recent = recent.sort_values('source')
    # Keep first entry of source 
    recent = recent.drop_duplicates(subset ="group", keep = 'first') 
    print("number of unique links: ",len(recent))

except FileNotFoundError:
    print('grouplinks_daily.csv does not exist')
    sys.exit()


try:    
    # Read master file with all historical links
    master = pandas.read_csv('groupsLinks_master.csv')
    print("Original Length of Master File: ", len(master))
    # Compare files and add new links to master file
    # Do not do left join because the website might also be deleting links. But the master roster should still contain the links. 
    common = master.merge(recent,on=['group'])
    new = recent[~recent['group'].isin(common['group'])]
    print("Number of New Links Added:", len(new))
    master = master.append(new)
    print("New Length of Master File: ", len(master))
    
    # Convert array to string:
    slack_str = new['group'].astype(str)

    # If no new links found:
    if len(slack_str)==0:
        response = requests.post('https://hooks.slack.com/services/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', json = {'text':'No New Links Found'})
        #print('Response code: ' + str(response.status_code))


except FileNotFoundError:
    print('grouplinks_master.csv does not exist. Creating master file from today\'s daily file ')
    master = recent
    slack_str = master['group'].astype(str)

## Concatenate all links to string and push to slack:
if len(slack_str) !=  0:
    # concatenate all links
    s = ', '
    slack_str = s.join(slack_str)
    print(slack_str)
    slack_data = {'text': slack_str}

    ## Push new links to slack
    response = requests.post('https://hooks.slack.com/services/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', json = slack_data)
    print('Response code: ' + str(response.status_code))

# Update master file 
master.to_csv(r'groupsLinks_master.csv', index = None, header=True)
