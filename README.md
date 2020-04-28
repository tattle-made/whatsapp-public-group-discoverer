## Why does this exist?

WhatsApp is one of the most popular platforms for communication in the country. One of Tattle's goals is to create an archive of content circulated on chat apps such as WhatsApp. For WhatsApp in particular, one way to collect content is to join 'public groups' as per Kiran et al's methodology: https://arxiv.org/abs/1804.01473

But before joining public groups we must know which groups can be joined. This scraper crawls a website that aggregates public WhatsApp group links and surfaces new public groups.  

*Note*: Tattle has temporarily stopped collecting content from Public WhatsApp Groups. We will resume after revising our strategy for content collection so that it balances concerns regarding user consent on WhatsApp group conversations. 

## Introduction 
This scraper scrapes a (website)[whatsappgrouplinks.org] that aggregates public WhatsApp group links and updates the new group links to a CSV file. 

The shell script can also be run at regular intervals via a cron job.

## Running Locally:
### Prerequisites:
Install [Scrapy Library](https://scrapy.org/) and all the requisite Python libraries.

### Steps to Run:
Run the shell script runWglScraper.sh. The execution can take several minutes.

The scraper can also be set to push the new links to a slack channel. Insert the webhook of the slack bot in trialDBUpdate.py (line 40 and line 58)


## Code Structure
The scraper scrapes (whatsappgrouplinks.org)[whatsappgrouplinks.org] and surfaces new whatsapp group links. These links are added to groupsLinks_master.csv

If the scraper is running for the first time, then all the links on the website will be added to the csv file. On subsequent iterations, only those links that were added to the website after the last run of the scraper will be appended to groupsLinks_master.csv. The new links found on the latest run of the scraper can be found on groupsLinks_daily.csv

runWglScraper.sh is shell script that executes the following steps:
* Deletes the old 'groupsLinks_daily.csv'. After the scraper is run a new file will be created.
* Runs the (Scrapy spider)[https://github.com/tattle-made/whatsapp-public-group-discoverer/blob/master/wgl_scraper/wgl_scraper/spiders/WAScraper.py]  to crawl whatsappgrouplinks.org
* Updates the csv files with new links. 

### Scrapy Spider
The operation of the spider is defined in (WAScraper.py)[https://github.com/tattle-made/whatsapp-public-group-discoverer/blob/master/wgl_scraper/wgl_scraper/spiders/WAScraper.py].

The spider goes through pages on the website and extracts links that contain 'https://chat.whatsapp.com/'.

The spider excludes pages defined in the variable 'deny'. In Tattle's case, this list excludes pages that might contain groups with sexually explicit content that Tattle does not want to archive content from. 


## Contribute
Please see instructions (here)[https://github.com/tattle-made/docs/blob/master/CONTRIBUTE.md].

## Get help with developing

Join our [Slack channel](https://join.slack.com/t/tattle-workspace/shared_invite/zt-da07n75v-kIw9Z5b~_gDKP~JsScP1Vg) to get someone to respond to immediate doubts and queries.

## Want to get help deploying it into your organisation?

Contact us at admin@tattle.co.in or ping us on [Slack channel](https://join.slack.com/t/tattle-workspace/shared_invite/zt-da07n75v-kIw9Z5b~_gDKP~JsScP1Vg)

## Licence
When you submit code changes, your submissions are understood to be under the same licence that covers the project - GPL-3. Feel free to contact the maintainers if that's a concern.


