# OCDS Scrapy Crawlers

This repo contains crawlers for OCDS data from various publishers, using the [Scrapy](https://scrapy.org/) crawler framework. 

Initially sources are based on those in [OCDS Kingfisher](https://github.com/open-contracting/kingfisher).

## Use
```
 pip install -r requirements.txt 

 scrapy crawl <spider_name> -a key=value
```
Currently implemented:

```
 scrapy crawl canada_buyandsell -a sample=true
 scrapy crawl canada_buyandsell
```

## Output

Currently scraped JSON is stored on disc, as it was found. Files are stored in `{project_root}/data/{scraper_name}/{datetime}`. The `/data/` part can be configured in `settings.py` with `FILES_STORE`.

## Deployment

Make sure `scrapyd` is running on the same server as the scrapers, and the URI and port in `scrapy.cfg` are configured correctly.

1. `git pull` if necessary to get the latest spiders.
1. Install dependencies: `pip install -r requirements-deploy.txt` (ie. the `scrapyd-client`) (or maybe `pip3 install scrapyd-client==1.2.0a1` if that doesn't work..).
1. `scrapyd-deploy -p kingfisher_scrapy` will make the spiders available to `scrapyd`.
1. List spiders: `scrapyd-client spiders -p kingfisher_scrapy`.
1. Schedule them to run: `scrapyd-client schedule -p kingfisher_scrapy \*`

Important note: when the crawlers are scheduled through `scrapyd` the output files appear in the `data` directory in the root of the `scrapyd` config (ie. beside the `eggs` etc), NOT in `data` from this repo.