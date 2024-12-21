pkgname = "unicode-cldr-common"
pkgver = "46.1"
pkgrel = 0
pkgdesc = "Common data from Unicode CLDR"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Unicode-DFS-2016"
url = "https://cldr.unicode.org"
source = f"https://github.com/unicode-org/cldr/archive/refs/tags/release-{pkgver.replace('.', '-')}.tar.gz"
sha256 = "56287d1e0380870e880162cc291f12fff6d598f22df86e3c40747670c6cd5b90"


def install(self):
    self.install_dir("usr/share/unicode/cldr")
    self.install_files("common", "usr/share/unicode/cldr")
