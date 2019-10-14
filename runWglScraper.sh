# Bash Script to Run Crawler
cd wgl_scraper/
rm -f groupsLinks_daily.csv
/usr/local/bin/scrapy crawl wgl  && 
/usr/bin/python3 trialDBUpdate.py
echo "scrapy run completed. Data base updated"
