from itemadapter import ItemAdapter
import psycopg2

class CommunityCommentsPipeline:
    def open_spider(self, spider):
        self.connection = psycopg2.connect(
            host='localhost',
            user='your_username',
            password='your_password',
            database='your_database')
        self.cursor = self.connection.cursor()

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS scraped_data (
                id SERIAL PRIMARY KEY,
                title TEXT,
                description TEXT,
                url TEXT
            )
        ''')
        self.connection.commit()

    def close_spider(self, spider):
        self.connection.close()

    def process_item(self, item, spider):
        self.cursor.execute('''
            INSERT INTO scraped_data (title, description, url)
            VALUES (%s, %s, %s)
        ''', (item['title'], item['description'], item['url']))
        self.connection.commit()
        return item
    

class CommunityNamesPipeline:
    def open_spider(self, spider):
        self.connection = psycopg2.connect(
            host='localhost',
            user='your_username',
            password='your_password',
            database='your_database')
        self.cursor = self.connection.cursor()

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS CommunityNames (
                id SERIAL PRIMARY KEY,
                title TEXT,
                description TEXT,
                url TEXT
            )
        ''')
        self.connection.commit()

    def close_spider(self, spider):
        self.connection.close()

    def process_item(self, item, spider):
        self.cursor.execute('''
            INSERT INTO CommunityNames (id, names, discussions_count)
            VALUES (%s, %s, %s)
        ''', (item['id'], item['names'], item['discussions_count']))
        self.connection.commit()
        return item