import re
import pymysql


class DbSaver:
    def __init__(self):
        psw = input('Please input the password: ')
        self.conn = pymysql.connect(
            host='104.199.180.9',
            user='root',
            password=psw,
            database='covid',
            charset='utf8'
        )

    def close(self):
        self.conn.close()

    def save_countries(self, country_list: list) -> None:
        """
        Save country names to database
        :param country_list:
        """
        cur = self.conn.cursor()
        for country in country_list:
            name = country[0]
            cur.execute(
                "SELECT * FROM countries WHERE name = '%s';" % name
            )
            country_id = cur.fetchall()[0][0]
            cur.execute(
                "INSERT INTO provinces (country_id, name) VALUES (%s, '%s');"
                % (country_id, name)
            )
        self.conn.commit()
        cur.close()

    def save_provinces(self, china_list: list, usa_list: list) -> None:
        """
        Save province names to database
        :param china_list: provinces in china
        :param usa_list: states in USA
        """
        cur = self.conn.cursor()
        for c in china_list:
            country_id = 1
            name = c[0]
            cur.execute(
                "INSERT INTO provinces (country_id, name) VALUES (%s, '%s');"
                % (country_id, name)
            )
        for u in usa_list:
            country_id = 2
            name = u[0]
            cur.execute(
                "INSERT INTO provinces (country_id, name) VALUES (%s, '%s');"
                % (country_id, name)
            )
        self.conn.commit()
        cur.close()

    def save_data(self, res: list, source_id: int) -> None:
        """
        Save covid data to database
        :param res: covid data
        :param source_id: source id
        """
        cur = self.conn.cursor()
        for d in res:
            name = d[0]
            cur.execute(
                "SELECT id FROM provinces WHERE name = '%s';" % name
            )
            province_id = cur.fetchall()[0][0]
            cur.execute(
                "INSERT INTO data (province_id, source_id, infected, suspected, cured, died)"
                "VALUES (%s, %s, %s, %s, %s, %s);"
                % (province_id, source_id, d[1], d[2], d[3], d[4])
            )
        self.conn.commit()
        cur.close()

    def save_news(self, res: dict) -> None:
        """
        Save news to database
        :param res: news dict
        """
        cur = self.conn.cursor()
        title = res['title']
        if len(title) > 110:
            title = title[:110]
        brief = res['content'][:1000]
        source = res['source']
        cur.execute(
            "INSERT INTO news (title, brief, source)"
            "VALUES ('%s', '%s', '%s');"
            % (title, brief, source)
        )
        self.conn.commit()
        cur.close()
