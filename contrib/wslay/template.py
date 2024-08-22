pkgname = "wslay"
pkgver = "1.1.1"
pkgrel = 0
build_style = "gnu_configure"
make_dir = "."
hostmakedepends = [
    "automake",
    "pkgconf",
    "python-sphinx",
    "slibtool",
]
pkgdesc = "WebSocket library in C"
maintainer = "Erica Z <zerica@callcc.eu>"
license = "MIT"
url = "https://tatsuhiro-t.github.io/wslay"
source = f"https://github.com/tatsuhiro-t/wslay/archive/refs/tags/release-{pkgver}.tar.gz"
sha256 = "7b9f4b9df09adaa6e07ec309b68ab376c0db2cfd916613023b52a47adfda224a"


def post_install(self):
    self.install_license("COPYING")


@subpackage("wslay-devel")
def _(self):
    return self.default_devel()
