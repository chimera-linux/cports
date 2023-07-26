pkgname = "unicode-cldr-common"
pkgver = "43.1"
pkgrel = 0
pkgdesc = "Common data from Unicode CLDR"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Unicode-DFS-2016"
url = "https://cldr.unicode.org"
source = f"https://github.com/unicode-org/cldr/archive/refs/tags/release-{pkgver.replace('.', '-')}.tar.gz"
sha256 = "0b063164ec434c150ff5f41699081ab0e4d9bf85c15a74f81f4b972b67d26bdb"


def do_install(self):
    self.install_dir("usr/share/unicode/cldr")
    self.install_files("common", "usr/share/unicode/cldr")
