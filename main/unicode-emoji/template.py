pkgname = "unicode-emoji"
pkgver = "14.0"
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
    "5432b76b57de3f6458ce0ffb91256c7427b3985ab3bc2398a5ae8c2a8bbc9d26",
    "ec474be073670aa7ce6dc1de9025b9fbb9b875fc63df815c254a5d1686fc6109",
    "bd2a7bd4ad4d50104054923ed406c5904fe587177295a84c67ec665d80921a68",
]

def do_install(self):
    for f in self.cwd.glob("*.txt"):
        self.install_file(f, "usr/share/unicode/emoji")
