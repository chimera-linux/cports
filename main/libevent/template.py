pkgname = "libevent"
pkgver = "2.1.13"
pkgrel = 0
build_style = "gnu_configure"
# regenerated configure gets stuck
configure_gen = []
hostmakedepends = ["pkgconf"]
makedepends = ["openssl3-devel"]
pkgdesc = "Abstract asynchronous event notification library"
license = "BSD-3-Clause"
url = "https://libevent.org"
source = f"https://github.com/libevent/libevent/releases/download/release-{pkgver}-stable/libevent-{pkgver}-stable.tar.gz"
sha256 = "f7e9383b8c0baa81b687e5b5eecc01beefaf1b19b64151d95ed61647fe7a315c"
hardening = ["!vis", "!cfi"]
# test suite does not like our env
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")


@subpackage("libevent-devel")
def _(self):
    return self.default_devel()
