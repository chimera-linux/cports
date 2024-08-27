pkgname = "unicode-character-database"
pkgver = "16.0.0"
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
    "cb1c663d053926500cd501229736045752713a066bd75802098598b7a7056177",
    "a0226610e324bcf784ac380e11f4cbf533ee1e6b3d028b0991bf8c0dc3f85853",
]


def do_install(self):
    self.install_dir("usr/share/unicode/ucd")

    for f in self.cwd.iterdir():
        self.install_files(f, "usr/share/unicode/ucd")
