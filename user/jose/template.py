pkgname = "jose"
pkgver = "14"
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
sha256 = "3ffb8ea9a0fa5194051499d96bfde957621fcd490ef7ed95effc699029d7ad3b"
# vis breaks symbols
hardening = ["!vis", "!cfi"]


@subpackage("jose-devel")
def _(self):
    return self.default_devel()
