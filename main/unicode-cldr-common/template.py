pkgname = "unicode-cldr-common"
pkgver = "42.0"
pkgrel = 0
pkgdesc = "Common data from Unicode CLDR"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Unicode-DFS-2016"
url = "https://cldr.unicode.org"
source = f"https://github.com/unicode-org/cldr/archive/refs/tags/release-{pkgver[:-2]}.tar.gz"
sha256 = "a65de26e4595be980142590dbd33f3768e78f8c52cc0b15b45c03f20043d5ea7"


def do_install(self):
    self.install_dir("usr/share/unicode/cldr")
    self.install_files("common", "usr/share/unicode/cldr")
