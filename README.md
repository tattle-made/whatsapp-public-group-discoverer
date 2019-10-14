# WhatsAppGroupLinksScraper
This scraper scrapes a website that aggregates public WhatsApp group links, daily and updates the new group links on the groupsLinks_master.csv. The links scraped on the day can be found on groupLinks_daily.csv. 

The scraper can also be set to push the new links to a slack channel. Insert the webhook of the slack bot in trialDBUpdate.py (line 40 and line 58)