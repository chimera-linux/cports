pkgname = "unicode-emoji"
pkgver = "15.0"
pkgrel = 0
pkgdesc = "Unicode Emoji data files"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Unicode-DFS-2016"
url = "https://home.unicode.org/emoji"
source = [
    f"https://www.unicode.org/Public/emoji/{pkgver}/emoji-sequences.txt",
    f"https://www.unicode.org/Public/emoji/{pkgver}/emoji-test.txt",
    f"https://www.unicode.org/Public/emoji/{pkgver}/emoji-zwj-sequences.txt",
]
sha256 = [
    "5c2222d8a432d896a031a68c2f54b04fbf47b0fce2e69853f1eb8a3e945eb56d",
    "8445f23ac8388e096be19d0262e14fceff856ff52093f2356dc89485f1a853db",
    "fe357f9117b7746676063765d587137edf9b25903a792bd54935bf0856791182",
]


def do_install(self):
    for f in self.cwd.glob("*.txt"):
        self.install_file(f, "usr/share/unicode/emoji")
