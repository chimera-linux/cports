pkgname = "gumbo-parser"
pkgver = "0.12.1"
pkgrel = 0
build_style = "gnu_configure"
configure_gen = ["./autogen.sh"]
make_cmd = "gmake"
hostmakedepends = [
    "automake",
    "gm4",
    "gmake",
    "libtool",
    "pkgconf",
]
makedepends = ["gtest-devel"]
pkgdesc = "HTML5 parsing library in pure C99"
maintainer = "ttyyls <contact@behri.org>"
license = "Apache-2.0"
url = "https://codeberg.org/grisha/gumbo-parser"
source = f"{url}/archive/{pkgver}.tar.gz"
sha256 = "a0ff2e1b613403fe69ff6407f3f93221fdfa67da357be158bb1e6903b33c1c10"


@subpackage("gumbo-parser-devel")
def _devel(self):
    return self.default_devel()
