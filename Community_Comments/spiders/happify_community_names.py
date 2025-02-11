import scrapy,json
from scrapy import Item, Field

class GroupItem(Item):
    id = Field()
    name = Field()
    discussions_count = Field()

class Happify_Names(scrapy.Spider):
    name = "happify_community_names"
    allowed_domains = ["https://my.happify.com"]
    start_urls = ["https://my.happify.com/api/forums/featured"]

    custom_settings = {
        'ITEM_PIPELINES': {
            'Community_Comments.pipelines.CommunityNamesPipeline': 300,
        }
    }

    cookies = {
        'marty_session_id': '39028e8c-02d1-41fc-80c2-32df77c3a5a4',
        'marty_session_id_hash': '6a37d280403d354fde6f0a4e079ca195',
        '_ga': 'GA1.1.1468845700.1739179850',
        '__utmz': '53476785.1739179851.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)',
        'current_environment': 'Prod',
        '_fbp': 'fb.1.1739179851967.323456223653154142',
        'remember_token': '4542110|94cea23051a1a11fd231b965c268cb3dfc3f2dc2',
        'happifyMixpanelCookie': 'b47a5074-ce3d-11ef-9a24-12241e6cca6e',
        'user_id_hash': '22faca513b8e6b3cf9581af610d720e2',
        '__utma': '53476785.1468845700.1739179850.1739179851.1739195139.2',
        '__utmc': '53476785',
        '__utmt': '1',
        'referrer': '%2F',
        'carousel_shown_track_4542110': '387',
        '_ga_T61WRQ8M1S': 'GS1.1.1739195138.3.1.1739195237.57.0.0',
        'mp_9975a59120353c375a7d289108bed4b0_mixpanel': '%7B%22distinct_id%22%3A%20%22b47a5074-ce3d-11ef-9a24-12241e6cca6e%22%2C%22%24device_id%22%3A%20%22194ef327d3c1aea-093c14bdf96485-14462c6e-1fa400-194ef327d3c1aeb%22%2C%22%24user_id%22%3A%20%22b47a5074-ce3d-11ef-9a24-12241e6cca6e%22%2C%22%24initial_referrer%22%3A%20%22%24direct%22%2C%22%24initial_referring_domain%22%3A%20%22%24direct%22%2C%22device_name%22%3A%20%22unknown%22%2C%22device_type%22%3A%20%22desktop%22%2C%22os%22%3A%20%22Linux%22%2C%22browser_name%22%3A%20%22Chrome%22%2C%22browser_version%22%3A%20%22133.0.0.0%22%2C%22browser_type%22%3A%20%22desktop%22%2C%22platform%22%3A%20%22Linux%20x86_64%22%2C%22__mps%22%3A%20%7B%7D%2C%22__mpso%22%3A%20%7B%7D%2C%22__mpus%22%3A%20%7B%7D%2C%22__mpa%22%3A%20%7B%7D%2C%22__mpu%22%3A%20%7B%7D%2C%22__mpr%22%3A%20%5B%5D%2C%22__mpap%22%3A%20%5B%5D%2C%22mp_name_tag%22%3A%20%22rohit71299%22%2C%22is_staff%22%3A%20false%2C%22user_id%22%3A%204542110%2C%22created_at_month%22%3A%20%222025_01%22%2C%22created_at_week%22%3A%20%222025_2%22%2C%22signup_referrer_landing_page_id%22%3A%200%2C%22created_at%22%3A%20%2220250109%22%2C%22signup_landing_page_id%22%3A%200%2C%22partner_space_id%22%3A%20null%2C%22partner_space_name%22%3A%20null%7D',
        '__utmb': '53476785.9.9.1739195148610',
        }

    headers = {
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'content-type': 'application/json',
        'referer': 'https://my.happify.com/community/',
    }

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(
                url=url,
                headers=self.headers,
                cookies=self.cookies,
                callback=self.parse
            )

    def __init__(self):
        pass

    def parse(self, response):
        groups = json.loads(response.body)
        for group in groups:
            id = group['id']
            name = group['name']
            discussions_count = group['num_discussions']
            item = GroupItem(id=id, name=name, discussions_count=discussions_count)
            yield item
            
    

