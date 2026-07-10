pkgname = "jose"
pkgver = "15"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "asciidoc",
    "libxml2-progs",
    "meson",
    "pkgconf",
]
makedepends = [
    "jansson-devel",
    "openssl3-devel",
    "zlib-ng-compat-devel",
]
checkdepends = ["jq"]
pkgdesc = "JSON Object Signing and Encryption standards in C"
license = "GPL-3.0-or-later"
url = "https://github.com/latchset/jose"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "d480f1f30dc11b7e81cd2939f9f0ef512090b131a11f68595483a2de0550fa89"
# vis breaks symbols
hardening = ["!vis", "!cfi"]


@subpackage("jose-devel")
def _(self):
    return self.default_devel()
