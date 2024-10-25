pkgname = "unicode-cldr-common"
pkgver = "46"
pkgrel = 0
pkgdesc = "Common data from Unicode CLDR"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Unicode-DFS-2016"
url = "https://cldr.unicode.org"
source = f"https://github.com/unicode-org/cldr/archive/refs/tags/release-{pkgver.replace('.', '-')}.tar.gz"
sha256 = "38d1c932835087749f278e2b835dd00b8706a4fe526f16ddc4b05a11ab839917"


def install(self):
    self.install_dir("usr/share/unicode/cldr")
    self.install_files("common", "usr/share/unicode/cldr")
