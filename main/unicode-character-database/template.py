pkgname = "unicode-character-database"
pkgver = "15.0.0"
pkgrel = 0
pkgdesc = "Unicode Character Database"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Unicode-DFS-2016"
url = "https://www.unicode.org"
source = [
    f"https://www.unicode.org/Public/zipped/{pkgver}/UCD.zip",
    f"https://www.unicode.org/Public/zipped/{pkgver}/Unihan.zip",
]
sha256 = [
    "5fbde400f3e687d25cc9b0a8d30d7619e76cb2f4c3e85ba9df8ec1312cb6718c",
    "24b154691fc97cb44267b925d62064297086b3f896b57a8181c7b6d42702a026",
]


def do_install(self):
    self.install_dir("usr/share/unicode/ucd")

    for f in self.cwd.iterdir():
        self.install_files(f, "usr/share/unicode/ucd")
