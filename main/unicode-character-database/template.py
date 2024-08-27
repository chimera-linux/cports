pkgname = "unicode-character-database"
pkgver = "16.0.0"
pkgrel = 1
pkgdesc = "Unicode Character Database"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Unicode-DFS-2016"
url = "https://www.unicode.org"
source = [
    f"https://www.unicode.org/Public/zipped/{pkgver}/UCD.zip>UCD-{pkgver}.zip",
    f"https://www.unicode.org/Public/zipped/{pkgver}/Unihan.zip>Unihan-{pkgver}.zip",
]
sha256 = [
    "c86dd81f2b14a43b0cc064aa5f89aa7241386801e35c59c7984e579832634eb2",
    "b8f000df69de7828d21326a2ffea462b04bc7560022989f7cc704f10521ef3e0",
]


def do_install(self):
    self.install_dir("usr/share/unicode/ucd")

    for f in self.cwd.iterdir():
        self.install_files(f, "usr/share/unicode/ucd")
