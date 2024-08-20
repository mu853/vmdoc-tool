import scrapy
import codecs
from nsxdiff.items import NsxdiffItem


class NsxdiffSpiderSpider(scrapy.Spider):
    name = "nsxdiff_spider"
    allowed_domains = ["docs.vmware.com"]
    version = "4.0"
    base = "VMware-NSX"
    #version = "3.1"
    #base = "VMware-NSX-T-Data-Center"

    start_urls = [
        "https://docs.vmware.com/en/base/version/administration/GUID-BB26CDC8-2A90-4C7E-9331-643D13FEEC4A.html".replace("version", version).replace("base", base),
        "https://docs.vmware.com/en/base/version/administration/GUID-E9E62E02-C226-457D-B3A6-FE71E45628F7.html".replace("version", version).replace("base", base),
        "https://docs.vmware.com/en/base/version/administration/GUID-6244CFD2-4119-4718-BA52-1BC9682A8C6E.html".replace("version", version).replace("base", base),
        "https://docs.vmware.com/en/base/version/administration/GUID-316E5027-E588-455C-88AD-A7DA930A4F0B.html".replace("version", version).replace("base", base),
        "https://docs.vmware.com/en/base/version/administration/GUID-DAB392AC-901E-4A61-8C30-5B6053D5C1CF.html".replace("version", version).replace("base", base),
        "https://docs.vmware.com/en/base/version/administration/GUID-A3674EA2-F368-4A53-9078-0694F76624F4.html".replace("version", version).replace("base", base),
        "https://docs.vmware.com/en/base/version/administration/GUID-A8B113EC-3D53-41A5-919E-78F1A3705F58.html".replace("version", version).replace("base", base),
        "https://docs.vmware.com/en/base/version/administration/GUID-7AD2C384-4303-4D6C-A44A-DEF45AA18A92.html".replace("version", version).replace("base", base),
        "https://docs.vmware.com/en/base/version/administration/GUID-FE14188D-9854-417F-9858-85F1867DAC71.html".replace("version", version).replace("base", base),
        "https://docs.vmware.com/en/base/version/administration/GUID-F0C4A33A-2B1F-43AA-94E1-602B628AFD52.html".replace("version", version).replace("base", base),
        "https://docs.vmware.com/en/base/version/administration/GUID-69DF29A3-746F-4D87-B430-C0E72B672459.html".replace("version", version).replace("base", base),
        "https://docs.vmware.com/en/base/version/administration/GUID-0AF89703-5357-4C24-8E66-06E56D5B4DF9.html".replace("version", version).replace("base", base),
        "https://docs.vmware.com/en/base/version/administration/GUID-C10D3FCE-754B-489B-86EB-D7373B228FF7.html".replace("version", version).replace("base", base),
        "https://docs.vmware.com/en/base/version/administration/GUID-A27DF20A-5162-40F5-B7D5-2DF8B6AE5DBE.html".replace("version", version).replace("base", base),
        "https://docs.vmware.com/en/base/version/administration/GUID-F29162C5-A5D9-4873-856D-FB5CD548EEC2.html".replace("version", version).replace("base", base),
        "https://docs.vmware.com/en/base/version/administration/GUID-F206A4B8-0F33-482D-8727-E71FE253BBCD.html".replace("version", version).replace("base", base),
        "https://docs.vmware.com/en/base/version/administration/GUID-50A6CAD9-D88B-47AD-A8FA-D9A76242C9A2.html".replace("version", version).replace("base", base),
        "https://docs.vmware.com/en/base/version/administration/GUID-F3A0A27E-88C0-4A64-8754-33CED93985D3.html".replace("version", version).replace("base", base),
        "https://docs.vmware.com/en/base/version/administration/GUID-F7589038-AFF2-459A-BE46-BF557CDFB9E4.html".replace("version", version).replace("base", base),
        "https://docs.vmware.com/en/base/version/administration/GUID-E3657F90-7291-4CE1-A52E-3D44490CED52.html".replace("version", version).replace("base", base),
        "https://docs.vmware.com/en/base/version/administration/GUID-33584FA9-78D0-40CD-975A-6363D13E5293.html".replace("version", version).replace("base", base),
        "https://docs.vmware.com/en/base/version/administration/GUID-1CAC911E-A224-4521-A9A2-0D668B4BFB61.html".replace("version", version).replace("base", base),
        "https://docs.vmware.com/en/base/version/administration/GUID-C47D8468-6A91-42EA-B8AC-63743F86C1E4.html".replace("version", version).replace("base", base),
        "https://docs.vmware.com/en/base/version/administration/GUID-9197EF8A-7998-4D1B-B968-067007C56B5C.html".replace("version", version).replace("base", base),
        "https://docs.vmware.com/en/base/version/administration/GUID-9CF6CB0E-DD94-4FCD-9B84-2BAE2DE4B95C.html".replace("version", version).replace("base", base),
        "https://docs.vmware.com/en/base/version/administration/GUID-A0B3667C-FB7D-413F-816D-019BFAD81AC5.html".replace("version", version).replace("base", base),
        "https://docs.vmware.com/en/base/version/administration/GUID-E6FE0C10-6F2A-4BAA-9973-4B2804B17095.html".replace("version", version).replace("base", base),
        "https://docs.vmware.com/en/base/version/administration/GUID-2A410298-6E09-4951-80D9-42D42F4F9D72.html".replace("version", version).replace("base", base)
    ]

#def __init__(self, *args, **kwargs):
#        super().__init__(*args, **kwargs)
#        for url in start_urls:
#            url.replace("/version/", self.version)

    def parse(self, response):
        guid = response.xpath('//head/meta[@name="guid"]/@content').get()
        language = response.xpath('//head/meta[@name="language"]/@content').get()
        version = response.url.split("/")[5]
        yield NsxdiffItem(
            url = response.url,
            title = response.xpath('//head/meta[@name="title"]/@content').get(),
            language = language,
            version = response.xpath('//head/meta[@name="primary-product-version"]/@content').get(),
            last_modified = response.xpath('//head/meta[@name="last modified"]/@content').get(),
            guid = guid
        )

        print(response.text, file=codecs.open("data/" + version + "/" + language + "/" + guid + ".html", 'w', 'utf-8'))
        for link in response.xpath('//ul[@class="ullinks"]/li/strong/a/@href'):
            url = response.urljoin(link.get())
            yield scrapy.Request(url, callback=self.parse)
        if '/en/' in response.url:
            url = response.url.replace('/en/', '/jp/')
            yield scrapy.Request(url, callback=self.parse)
