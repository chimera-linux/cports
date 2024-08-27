pkgname = "unicode-emoji"
pkgver = "16.0"
pkgrel = 1
pkgdesc = "Unicode Emoji data files"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Unicode-DFS-2016"
url = "https://home.unicode.org/emoji"
source = [
    f"https://www.unicode.org/Public/emoji/{pkgver}/emoji-sequences.txt>emoji-sequences-{pkgver}.txt",
    f"https://www.unicode.org/Public/emoji/{pkgver}/emoji-test.txt>emoji-test-{pkgver}.txt",
    f"https://www.unicode.org/Public/emoji/{pkgver}/emoji-zwj-sequences.txt>emoji-zwj-sequences-{pkgver}.txt",
]
sha256 = [
    "3fe3c77e72e8f26df302dc7d99b106c5d08fd808ef7246fb5d4502d659fe659c",
    "24f0c534e86cf142e2496953e8f0e46a3e702392911eddcd29c6cced85139697",
    "9423ec235474356f970a696506737e2d5d65453a67f45df66b8bbe920c3fab83",
]


def do_install(self):
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
