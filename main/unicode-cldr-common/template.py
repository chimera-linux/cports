pkgname = "unicode-cldr-common"
pkgver = "44"
pkgrel = 0
pkgdesc = "Common data from Unicode CLDR"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Unicode-DFS-2016"
url = "https://cldr.unicode.org"
source = f"https://github.com/unicode-org/cldr/archive/refs/tags/release-{pkgver.replace('.', '-')}.tar.gz"
sha256 = "0fce28d993d85a4b3f6ebae3179a08dddcd4d28e87bfe922bab71d513f79abf2"


def do_install(self):
    self.install_dir("usr/share/unicode/cldr")
    self.install_files("common", "usr/share/unicode/cldr")
