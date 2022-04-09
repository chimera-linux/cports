pkgname = "unicode-cldr-common"
pkgver = "41.0"
pkgrel = 0
pkgdesc = "Common data from Unicode CLDR"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Unicode-DFS-2016"
url = "https://cldr.unicode.org"
source = f"https://github.com/unicode-org/cldr/releases/download/release-{pkgver[:-2]}/cldr-common-{pkgver}.zip"
sha256 = "823c6170c41e2de2c229574e8a436332d25f1c9723409867fe721e00bc92d853"

def do_install(self):
    self.install_dir("usr/share/unicode/cldr")
    self.install_files("common", "usr/share/unicode/cldr")
    self.install_license("LICENSE.txt")
