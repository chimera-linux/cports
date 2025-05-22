pkgname = "unicode-cldr-common"
pkgver = "47"
pkgrel = 0
pkgdesc = "Common data from Unicode CLDR"
license = "Unicode-DFS-2016"
url = "https://cldr.unicode.org"
source = f"https://github.com/unicode-org/cldr/archive/refs/tags/release-{pkgver.replace('.', '-')}.tar.gz"
sha256 = "da858185edee37877c98951e12926970372eed45f209ef54a56b32013667bf9b"


def install(self):
    self.install_dir("usr/share/unicode/cldr")
    self.install_files("common", "usr/share/unicode/cldr")
