pkgname = "unicode-character-database"
pkgver = "14.0.0"
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
    "033a5276b5d7af8844589f8e3482f3977a8385e71d107d375055465178c23600",
    "2ae4519b2b82cd4d15379c17e57bfb12c33c0f54da4977de03b2b04bcf11852d",
]

def do_install(self):
    self.install_dir("usr/share/unicode/ucd")

    for f in self.cwd.iterdir():
        self.install_files(f, "usr/share/unicode/ucd")
