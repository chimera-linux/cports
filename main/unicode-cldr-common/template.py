pkgname = "unicode-cldr-common"
pkgver = "40.0"
pkgrel = 0
pkgdesc = "Common data from Unicode CLDR"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Unicode-DFS-2016"
url = "https://cldr.unicode.org"
source = f"https://github.com/unicode-org/cldr/releases/download/release-{pkgver[:-2]}/cldr-common-{pkgver}.zip"
sha256 = "8d03c1ba6a3e33280e3959a34fe37d0a7002a4b6ac40c6570a69f7bbc25e6756"

def do_install(self):
    self.install_dir("usr/share/unicode/cldr")
    self.install_files("common", "usr/share/unicode/cldr")
    self.install_license("LICENSE.txt")
