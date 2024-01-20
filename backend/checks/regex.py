import re


class RegexCheck:
    def __init__(self):
        self.patterns = [
            re.compile(
                r"(?!steamcommunity)s([trl](rea|e{1,2}[aemr]|ae)|e)(r[nm]|m{1,2}|n{1,2}|am|nm|mn|w)(c|[-_\\.]|[sa]){1,2}[oua]{1,2}[nmr]{1,5}(u{1,2}n{1,2}|um|ui|in|an|.[tyue])(.*[tlyi]y|.*tu|[iyt]{1,4})(r([uy])|[uev]){0,1}\\."),
            re.compile(
                r"\\/tr[aoe]+de?\\/?[ao0]ff?ers*\\/?(?:n[eo][wv]s*\\/?)?[?=]pa[nr]t?[nm]er[=-][?a-zA-Z0-9_-]+(?:&t[ao]ke[rnm][=-][?a-zA-Z0-9_-]+)?"),
            re.compile(r"(?i).*https?:\\/\\/(?!(www\\.)?discord)[^\\s]+\\.gift.*"),
            re.compile(
                r"(?i)^(?=.*https?:\\/\\/(?!(www\\.)?((cdn\\.)?discord(app)?\\.(com|gg)|discord\\.gift|(acer|amd|sapphiretech)\\.com))[^\\s]+\\.[^\\s])(?=.*\\b(?<![\\/\\-_&])(nitro|gift)\\b(?![\\/\\-_&]))(?!.*\\bacer\\b).*$"),
            re.compile(
                r"(?i)^(?=.*https?:\\/\\/(?!(www\\.)?steamcommunity\\.com)[^\\s]+\\.[^\\s])(?=.*\\b(?<![\\/\\-_&])(game|cs[: -]*go|give)\\b(?![\\/\\-_&]))(?=.*\\b(?<![\\/\\-_&])(inventory|kni[fv]es?|skins?)\\b(?![\\/\\-_&])).*$"),
            re.compile(
                r"(?i).*https?:\\/\\/(www\\.)?(partpicker\\.shop|sportshub\\.bar|locations\\.quest|shrekis\\.life|gamingfun\\.me|catsnthings?\\.(com|fun)|fortnight\\.space|grabify\\.link|(lovebird|trulove)\\.guru|(dateing|curiouscat)\\.club|(headshot|progaming|yourmy)\\.monster|(gaming-at-my|imageshare|screenshot)\\.best|(joinmy|fortnitechat)\\.site|(freegiftcards|stopify|leancoding)\\.co).*")
        ]

    def check_url(self, url):
        for pattern in self.patterns:
            if pattern.match(url):
                return True
        return False
