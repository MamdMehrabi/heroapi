import urllib.parse
import replicate
import html
import re
import requests
import random
import langdetect
import faker


def rubino(url: str, timeout: float = 10) -> dict:
    '''This method is used to get the download link
    and other information of the post(s) in Rubino Messenger
    :param url:
        The link of the desired post
    :param timeout:
        Optional To manage slow timeout when the server is slow
    :return:
        Full post information

    If you want more details, go to this address: https://github.com/metect/myrino
    '''
    auth_list: list = []
    payload: dict = {
        'api_version': '0',
        'auth': random.choice(seq=auth_list),
        'client': {
            'app_name': 'Main',
            'app_version': '3.0.1',
            'package': 'app.rubino.main',
            'lang_code': 'en',
            'platform': 'PWA'
    },
        'data': {
            'share_link': url.split('/')[-1],
            'profile_id': None
        },
        'method': 'getPostByShareLink'
    }
    session = requests.session()
    base_url: str = f'https://rubino{random.randint(1, 20)}.iranlms.ir/'
    return session.request('post', url=base_url, timeout=timeout, json=payload).json()


def font(text: str = 'ohmyapi') -> dict:
    '''This function is for generating fonts. Currently only English language is supported
    :param text:
        The text you want the font to be applied to
    '''
    fonts: dict = {
        "0": ["𝔞", "𝔟", "𝔠", "𝔡", "𝔢", "𝔣", "𝔤", "𝔥", "𝔦", "𝔧", "𝔨", "𝔩", "𝔪", "𝔫", "𝔬", "𝔭", "𝔮", "𝔯", "𝔰", "𝔱", "𝔲", "𝔳", "𝔴", "𝔵", "𝔶", "𝔷"],
        "1": ["𝓪", "𝓫", "𝓬", "𝓭", "𝓮", "𝓯", "𝓰", "𝓱", "𝓲", "𝓳", "𝓴", "𝓵", "𝓶", "𝓷", "𝓸", "𝓹", "𝓺", "𝓻", "𝓼", "𝓽", "𝓾", "𝓿", "𝔀", "𝔁", "𝔂", "𝔃"],
        "2": ["𝒶", "𝒷", "𝒸", "𝒹", "𝑒", "𝒻", "𝑔", "𝒽", "𝒾", "𝒿", "𝓀", "𝓁", "𝓂", "𝓃", "𝑜", "𝓅", "𝓆", "𝓇", "𝓈", "𝓉", "𝓊", "𝓋", "𝓌", "𝓍", "𝓎", "𝓏"],
        "3": ["𝕒", "𝕓", "𝕔", "𝕕", "𝕖", "𝕗", "𝕘", "𝕙", "𝕚", "𝕛", "𝕜", "𝕝", "𝕞", "𝕟", "𝕠", "𝕡", "𝕢", "𝕣", "𝕤", "𝕥", "𝕦", "𝕧", "𝕨", "𝕩", "𝕪", "𝕫"],
        "4": ["ᴀ", "ʙ", "ᴄ", "ᴅ", "ᴇ", "ꜰ", "ɢ", "ʜ", "ɪ", "ᴊ", "ᴋ", "ʟ", "ᴍ", "ɴ", "ᴏ", "ᴘ", "Q", "ʀ", "ꜱ", "ᴛ", "ᴜ", "ᴠ", "ᴡ", "x", "ʏ", "ᴢ"],
        "5": ["ⓐ", "ⓑ", "ⓒ", "ⓓ", "ⓔ", "ⓕ", "ⓖ", "ⓗ", "ⓘ", "ⓙ", "ⓚ", "ⓛ", "ⓜ", "ⓝ", "ⓞ", "ⓟ", "ⓠ", "ⓡ", "ⓢ", "ⓣ", "ⓤ", "ⓥ", "ⓦ", "ⓧ", "ⓨ", "ⓩ"],
        "6": ["𝐚", "𝐛", "𝐜", "𝐝", "𝐞", "𝐟", "𝐠", "𝐡", "𝐢", "𝐣", "𝐤", "𝐥", "𝐦", "𝐧", "𝐨", "𝐩", "𝐪", "𝐫", "𝐬", "𝐭", "𝐮", "𝐯", "𝐰", "𝐱", "𝐲", "𝐳"],
        "7": ["𝗮", "𝗯", "𝗰", "𝗱", "𝗲", "𝗳", "𝗴", "𝗵", "𝗶", "𝗷", "𝗸", "𝗹", "𝗺", "𝗻", "𝗼", "𝗽", "𝗾", "𝗿", "𝘀", "𝘁", "𝘂", "𝘃", "𝘄", "𝘅", "𝘆", "𝘇"],
        "8": ["𝒂", "𝒃", "𝒄", "𝒅", "𝒆", "𝒇", "𝒈", "𝒉", "𝒊", "𝒋", "𝒌", "𝒍", "𝒎", "𝒏", "𝒐", "𝒑", "𝒒", "𝒓", "𝒔", "𝒕", "𝒖", "𝒗", "𝒘", "𝒙", "𝒚", "𝒛"],
        "9": ["α", "ɓ", "૮", "∂", "ε", "ƒ", "ɠ", "ɦ", "เ", "ʝ", "ҡ", "ℓ", "ɱ", "ɳ", "σ", "ρ", "φ", "૨", "ร", "ƭ", "µ", "ѵ", "ω", "א", "ყ", "ƶ"],
        "10": ["【A】", "【B】", "【C】", "【D】", "【E】", "【F】", "【G】", "【H】", "【I】", "【J】", "【K】", "【L】", "【M】", "【N】", "【O】", "【P】", "【Q】", "【R】", "【S】", "【T】", "【U】", "【V】", "【W】", "【X】", "【Y】", "【Z】"],
        "11": ["⒜", "⒝", "⒞", "⒟", "⒠", "⒡", "⒢", "⒣", "⒤", "⒥", "⒦", "⒧", "⒨", "⒩", "⒪", "⒫", "⒬", "⒭", "⒮", "⒯", "⒰", "⒱", "⒲", "⒳", "⒴", "⒵"],
        "12": ["ᵃ", "ᵇ", "ᶜ", "ᵈ", "ᵉ", "ᶠ", "ᵍ", "ʰ", "ᶦ", "ʲ", "ᵏ", "ˡ", "ᵐ", "ⁿ", "ᵒ", "ᵖ", "ᑫ", "ʳ", "ˢ", "ᵗ", "ᵘ", "ᵛ", "ʷ", "ˣ", "ʸ", "ᶻ"],
        "13": ["Ⓐ", "Ⓑ", "Ⓒ", "Ⓓ", "Ⓔ", "Ⓕ", "Ⓖ", "Ⓗ", "Ⓘ", "Ⓙ", "Ⓚ", "Ⓛ", "Ⓜ", "Ⓝ", "Ⓞ", "Ⓟ", "Ⓠ", "Ⓡ", "Ⓢ", "Ⓣ", "Ⓤ", "Ⓥ", "Ⓦ", "Ⓧ", "Ⓨ", "Ⓩ"],
        "14": ["𝐀", "𝐁", "𝐂", "𝐃", "𝐄", "𝐅", "𝐆", "𝐇", "𝐈", "𝐉", "𝐊", "𝐋", "𝐌", "𝐍", "𝐎", "𝐏", "𝐐", "𝐑", "𝐒", "𝐓", "𝐔", "𝐕", "𝐖", "𝐗", "𝐘", "𝐙"],
        "15": ["𝕬", "𝕭", "𝕮", "𝕯", "𝕰", "𝕱", "𝕲", "𝕳", "𝕿", "𝕴", "𝕶", "𝕷", "𝕸", "𝕹", "𝕺", "𝕻", "𝕼", "𝕽", "𝕾", "𝕵", "𝖀", "𝖁", "𝖂", "𝖃", "𝚼", "𝖅"],
        "16": ["𝘼", "𝘽", "𝘾", "𝘿", "𝙀", "𝙁", "𝙂", "𝙃", "𝙄", "𝙅", "𝙆", "𝙇", "𝙈", "𝙉", "𝙊", "𝙋", "𝙌", "𝙍", "𝙎", "𝙏", "𝙐", "𝙑", "𝙒", "𝙓", "𝙔", "𝙕"],
        "17": ["𝓐", "𝓑", "𝓒", "𝓓", "𝓔", "𝓕", "𝓖", "𝓗", "𝓘", "𝓙", "𝓚", "𝓛", "𝓜", "𝓝", "𝓞", "𝓟", "𝓠", "𝓡", "𝓢", "𝓣", "𝓤", "𝓥", "𝓦", "𝓧", "𝓨", "𝓩"],
        "18": ["𝒜", "ℬ", "𝒞", "𝒟", "ℰ", "ℱ", "𝒢", "ℋ", "ℐ", "𝒥", "𝒦", "ℒ", "ℳ", "𝒩", "𝒪", "𝒫", "𝒬", "ℛ", "𝒮", "𝒯", "𝒰", "𝒱", "𝒲", "𝒳", "𝒴"],
        "19": ["𝔸", "𝔹", "ℂ", "𝔻", "𝔼", "𝔽", "𝔾", "ℍ", "𝕀", "𝕁", "𝕂", "𝕃", "𝕄", "ℕ", "𝕆", "ℙ", "ℚ", "ℝ", "𝕊", "𝕋", "𝕌", "𝕍", "𝕎", "𝕏", "𝕐", "ℤ"],
        "20": ["Ａ", "Ｂ", "Ｃ", "Ｄ", "Ｅ", "Ｆ", "Ｇ", "Ｈ", "Ｉ", "Ｊ", "Ｋ", "Ｌ", "Ｍ", "Ｎ", "Ｏ", "Ｐ", "Ｑ", "Ｒ", "Ｓ", "Ｔ", "Ｕ", "Ｖ", "Ｗ", "Ｘ", "Ｙ", "Ｚ"],
        "21": ["ᴀ", "ʙ", "ᴄ", "ᴅ", "ᴇ", "ғ", "ɢ", "ʜ", "ɪ", "ᴊ", "ᴋ", "ʟ", "ᴍ", "ɴ", "ᴏ", "ᴘ", "ǫ", "ʀ", "s", "ᴛ", "ᴜ", "ᴠ", "ᴡ", "x", "ʏ", "ᴢ"],
        "22": ["ᴬ", "ᴮ", "ᶜ", "ᴰ", "ᴱ", "ᶠ", "ᴳ", "ᴴ", "ᴵ", "ᴶ", "ᴷ", "ᴸ", "ᴹ", "ᴺ", "ᴼ", "ᴾ", "ᵟ", "ᴿ", "ˢ", "ᵀ", "ᵁ", "ⱽ", "ᵂ", "ˣ", "ᵞ", "ᶻ"],
        "23": ["卂", "乃", "匚", "刀", "乇", "下", "厶", "卄", "工", "丁", "长", "乚", "从", "𠘨", "口", "尸", "㔿", "尺", "丂", "丅", "凵", "リ", "山", "乂", "丫", "乙"],
        "24": ["『a』", "『b』", "『c』", "『d』", "『e』", "『f』", "『g』", "『h』", "『i』", "『j』", "『k』", "『l』", "『m』", "『n』", "『o』", "『p』", "『q』", "『r』", "『s』", "『t』", "『u』", "『v』", "『w』", "『x』", "『y』", "『z』"],
        "25": ["a♥", "b♥", "c♥", "d♥", "e♥", "f♥", "g♥", "h♥", "i♥", "j♥", "k♥", "l♥", "m♥", "n♥", "o♥", "p♥", "q♥", "r♥", "s♥", "t♥", "u♥", "v♥", "w♥", "x♥", "y♥", "z♥"],
        "26": ["𝕒", "β", "ς", "ᗪ", "𝑒", "𝔣", "𝔾", "ℍ", "ᶤ", "𝕁", "Ҝ", "ˡ", "𝕞", "ή", "𝔬", "Ⓟ", "𝐪", "Ř", "𝓢", "ţ", "Ｕ", "ᐯ", "ω", "𝔵", "ㄚ", "ｚ"],
        "27": ["Δ", "𝒷", "ς", "ⓓ", "𝒆", "𝓕", "𝑔", "ⓗ", "𝐢", "Ⓙ", "𝕜", "ℓ", "Ⓜ", "Ň", "Ø", "卩", "ợ", "𝓇", "ѕ", "ｔ", "𝐮", "𝓋", "𝔀", "𝕩", "у", "𝓩"],
        "28": ["𝔸", "ᵇ", "ς", "𝔻", "𝒆", "ƒ", "ģ", "ђ", "𝐢", "𝐉", "𝐤", "ˡ", "м", "ℕ", "ᵒ", "ק", "𝐪", "𝔯", "ร", "ⓣ", "ⓤ", "ｖ", "ᗯ", "𝕩", "ⓨ", "z"],
        "29": ["α", "𝔟", "ᑕ", "đ", "є", "ғ", "𝐠", "Ħ", "Ｉ", "𝓙", "к", "Ĺ", "м", "𝓝", "Ｏ", "ｐ", "𝓠", "𝓡", "𝔰", "ţ", "ù", "𝐕", "𝐰", "χ", "ｙ", "ž"],
        "30": ["𝒶", "𝒷", "𝔠", "Ｄ", "ｅ", "ⓕ", "g", "Ⓗ", "ί", "ڶ", "ⓚ", "𝓵", "𝕄", "ή", "𝑜", "Ƥ", "𝓠", "𝓻", "𝐒", "ⓣ", "Ｕ", "ש", "ｗ", "ｘ", "Ⓨ", "Ž"],
        "31": ["Ⓐ", "𝕓", "𝓬", "Đ", "ⓔ", "𝒇", "g", "𝕙", "เ", "Ｊ", "ᛕ", "ᒪ", "𝓂", "ⓝ", "𝕆", "Ƥ", "𝓆", "г", "𝐒", "т", "Ǘ", "𝐯", "Ŵ", "𝐗", "𝕪", "Ｚ"],
        "32": ["ⓐ", "𝔹", "𝐂", "Ⓓ", "𝒆", "ℱ", "Ⓖ", "Ｈ", "ᶤ", "𝐣", "ｋ", "Ⓛ", "𝓶", "Ň", "𝐎", "ⓟ", "ⓠ", "ʳ", "Ŝ", "ţ", "Ữ", "ｖ", "𝔴", "Ж", "¥", "ｚ"]
    }

    converted_text = ''
    for count in range(0, len(fonts)):
        for char in text:
            if char.isalpha():
                char_index = ord(char.lower()) - 97
                converted_text += fonts[str(count)][char_index]
            else:
                converted_text += char

        converted_text += '\n'
        result = converted_text.split('\n')[0:-1]

    return result


def lang(text: str) -> str:
    '''This function is to identify the language of a text
    :param text:
        Your desired text
    :return:
        example: `en` or `fa`
    '''
    try:
        return langdetect.detect(text)
    except langdetect.LangDetectException:
        return 'The value of the text parameter you sent is integer. While you should have sent string'


def translator(text: str, to_lang: str = 'auto', from_lang: str = 'auto') -> dict:
    '''This API, which is based on the Google Translate API, is used to translate texts'''
    session = requests.session()
    base_url: str = 'https://translate.google.com'
    url: str = f'{base_url}/m?tl={to_lang}&sl={from_lang}&q={urllib.parse.quote(text)}'
    r = session.request(
        method='get', url=url, headers={
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:47.0) Gecko/20100101 Firefox/47.0'
        }
    )

    if r.status_code == 200:
        result = re.findall(r'(?s)class="(?:t0|result-container)">(.*?)<', r.text)
        return html.unescape(result[0])
    else:
        return 'A problem has occurred'


def fake(count: int = 100, lang: str = 'en_US') -> str:
    '''This api is used to generate fake text
    :param count
        Number of words, example >>> `10`
    :param lang
        desired language, example >>> `en_US` or `fa_IR`

    '''
    text: list = []
    __fake = faker.Faker([lang])
    # for _ in range(0, count):
    #     text.append(__fake.text())

    return __fake.text(count)