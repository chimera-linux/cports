pkgname = "unicode-emoji"
pkgver = "17.0"
pkgrel = 0
pkgdesc = "Unicode Emoji data files"
license = "Unicode-DFS-2016"
url = "https://home.unicode.org/emoji"
source = [
    f"https://www.unicode.org/Public/emoji/{pkgver}/emoji-sequences.txt>emoji-sequences-{pkgver}.txt",
    f"https://www.unicode.org/Public/emoji/{pkgver}/emoji-test.txt>emoji-test-{pkgver}.txt",
    f"https://www.unicode.org/Public/emoji/{pkgver}/emoji-zwj-sequences.txt>emoji-zwj-sequences-{pkgver}.txt",
]
sha256 = [
    "bec5f82bc4c846ccba508b2c617aae239c0804dde0106f06eee62e011cb494f6",
    "07ee0565612af5d8cf36ea7d2cd7d255429441059133c60f863e97e648ebeb29",
    "5b25441daed2322b068c5e70cda522946a4f0274df864445a1965a92e5fc5cad",
]


def install(self):
    self.install_file(
        f"emoji-sequences-{pkgver}.txt",
        "usr/share/unicode/emoji",
        name="emoji-sequences.txt",
    )
    self.install_file(
        f"emoji-test-{pkgver}.txt",
        "usr/share/unicode/emoji",
        name="emoji-test.txt",
    )
    self.install_file(
        f"emoji-zwj-sequences-{pkgver}.txt",
        "usr/share/unicode/emoji",
        name="emoji-zwj-sequences.txt",
    )
