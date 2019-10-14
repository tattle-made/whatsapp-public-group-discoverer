# WhatsAppGroupLinksScraper

This scraper scrapes a website that aggregates public WhatsApp group links and updates the new group links on the groupsLinks_master.csv. The links scraped on the day can be found on groupLinks_daily.csv. 

The scraper can also be set to push the new links to a slack channel. Insert the webhook of the slack bot in trialDBUpdate.py (line 40 and line 58)

Run the shell script runWglScraper.sh to kick off the scraper. Note the scraper can take several minutes to finish execution.

The shell script can also be run at regulat intervals via a cron job.
