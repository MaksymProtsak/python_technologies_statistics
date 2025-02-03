from pathlib import Path

from typing import List
from urllib.parse import urljoin

import scrapy


class PythonTechnologiesSpider(scrapy.Spider):
    name = "technologies"

    def start_requests(self):
        urls = [
            "https://jobs.dou.ua/vacancies/",
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = f"quotes-{page}.html"
        Path(filename).write_bytes(response.body)
        self.log(f"Saved file {filename}")
