pkgname = "unicode-emoji"
pkgver = "16.0"
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
    "eb72c9115e3504fbbe1c8621b619f879471a46ccc56e2f445417b7c1cad050d1",
    "d876ee249aa28eaa76cfa6dfaa702847a8d13b062aa488d465d0395ee8137ed9",
    "9a76a03dcacfcd8f9bfe08c49c8d90b55182b977cbcc87a694e8a8193efb0e57",
]


def do_install(self):
    for f in self.cwd.glob("*.txt"):
        self.install_file(f, "usr/share/unicode/emoji")
