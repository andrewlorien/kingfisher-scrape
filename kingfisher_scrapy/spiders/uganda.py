import json

import scrapy


class Uganda(scrapy.Spider):
    name = 'Uganda'
    # TODO add missing tags 'award', 'contract'

    for tag in ['planning', 'tender']:
        start_urls = ['http://gpp.ppda.go.ug/api/v1/releases?tag=%s&page=1' % tag]

        def parse(self, response):
            data = json.loads(response.body)
            last_page = data['pagination']['last_page']

            for page in range(1, last_page + 1):
                file_url = 'http://gpp.ppda.go.ug/api/v1/releases?tag=%s&page=%d' % (self.tag, page)

                if hasattr(self, 'sample') and self.sample == 'true':
                    file_url = self.start_urls

                yield {
                    'file_urls': [file_url],
                    'data_type': 'release_package'
                }
