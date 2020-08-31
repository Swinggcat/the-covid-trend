import re
from pypinyin import lazy_pinyin


def to_pinyin(s: str) -> str:
    """
    Convert Chinese str to pinyin str
    :param s: chinese str
    :return: pinyin str
    """
    if s == '山西':
        return 'Shan1xi'
    elif s == '陕西':
        return 'Shan3xi'
    pylist = lazy_pinyin(s)
    py = ''.join(pylist)
    return py


def parse_usa(text: str, state: str) -> tuple:
    """
    Get covid data of each states in USA
    :param state: state
    :param text: text to be parsed
    :return: list of (state_name, confirmed, suspected, cured, dead)
    """
    pattern = re.compile(
        r'\"statistic-module--statistic--QKc9M\">.*?'
        r'\"statistic-module--title--MZHLl\">(.*?)<.*?'
        r'\"statistic-module--value--2qXQD.*?\">(.*?)<'
    )
    result = pattern.findall(text)
    final_result = [state.capitalize(), -1, -1, -1, -1]
    for i, res in enumerate(result):
        n = res[1].replace(',', '')
        if not n.isdigit():
            continue
        if res[0] == 'Total cases':
            final_result[1] = int(n)
        elif res[0] == 'Recovered':
            final_result[3] = int(n)
        elif res[0] == 'Deaths' or res[0] == 'Total deaths':
            final_result[4] = int(n)
    final_result = tuple(final_result)
    return final_result


def parse_china(text: str) -> list:
    """
    Get covid data of each provinces in china
    :param text: text to be parsed
    :return: (province_name, confirmed, suspected, cured, dead)
    """
    pattern = re.compile(
        r'\{\"provinceName\":\".*?\",'
        r'\"provinceShortName\":\"(.*?)\".*?'
        r'\"confirmedCount\":(.*?),.*?'
        r'\"suspectedCount":(.*?),'
        r'\"curedCount\":(.*?),'
        r'\"deadCount\":(.*?),'
    )
    result = pattern.findall(text)
    for i, res in enumerate(result):
        res = list(res)
        res[0] = to_pinyin(res[0]).capitalize()
        result[i] = tuple(res)
    return result


def parse_country(text: str) -> list:
    """
    Get covid data of each countries in the world
    :param text: text to be parsed
    :return: (country_name, confirmed, suspected, cured, dead, timestamp)
    """
    pattern = re.compile(
        r',\"provinceName\":\".*?\",.*?'
        r'\"confirmedCount\":(.*?),.*?'
        r'\"suspectedCount":(.*?),'
        r'\"curedCount\":(.*?),'
        r'\"deadCount\":(.*?),.*?'
        r'\"countryFullName\":\"(.*?)\",'
    )
    result = pattern.findall(text)
    for i, res in enumerate(result):
        res = list(res)
        n = res.pop()
        n = re.sub(r'\xa0', ' ', n)
        res.insert(0, n)
        result[i] = tuple(res)
    return result


def parse_news_index(text: str) -> list:
    """
    Get news url from the index page of WHO News
    :param text: text to be parsed
    :return: list of news urls
    """
    pattern = re.compile(r'<a href=\"(.*?)\"')
    result = pattern.findall(text)
    final_result = []
    for res in result:
        if len(res) > 16 and res[:17] == '/news-room/detail':
            final_result.append(res)
    return final_result


def parse_news_content(text: str) -> dict:
    """
    Get news details
    :param text: text to be parsed
    :return: dict of news, {'title': xxx, 'content': xxx, 'source': xxx}
    """
    # get title
    d = {}
    pattern = re.compile(r'h1.*?>(.*?)</h1')
    result = pattern.findall(text)
    d['title'] = result[0]

    # get content
    pattern = re.compile(r'p.*?>(.*?)</p')
    result = pattern.findall(text)
    new_result = []
    for i, res in enumerate(result):
        res = re.sub(r'&.*?;', '', res)
        res = re.sub(r'#.*?#', '', res)
        res = re.sub(r'\\n', '', res)
        res = re.sub(r'<.*?>(.*?)</.*?>', '', res)
        res = re.sub(r'<.*?>', '', res)
        res = re.sub(r'--+', '', res)
        res = re.sub(r'  +', ' ', res)
        res = re.sub(r',,+', ', ', res)
        if res == '':
            continue
        new_result.append(res)
    d['content'] = ''.join(new_result)

    d['source'] = 'WHO News Release'
    return d
