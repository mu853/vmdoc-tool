#!/bin/bash
version=$1
if [[ "$version" == "" ]]; then
  version='4.2'
fi

#scrapy crawl nsxdiff_spider -a version=4.2 -o summary.csv
scrapy crawl nsxdiff_spider -o summary.csv
