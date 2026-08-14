pkgname = "ragel"
pkgver = "7.0.4"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--with-colm=/usr",
    "--disable-manual",
    "--disable-static",
]
make_dir = "."
hostmakedepends = ["automake", "libtool", "colm"]
makedepends = ["colm-devel"]
checkdepends = ["bash"]
pkgdesc = "Finite state machine compiler"
license = "GPL-2.0-or-later"
url = "https://www.colm.net/open-source/ragel/index.html"
source = f"https://www.colm.net/files/ragel/ragel-{pkgver}.tar.gz"
sha256 = "84b1493efe967e85070c69e78b04dc55edc5c5718f9d6b77929762cb2abed278"


@subpackage("ragel-devel")
def _(self):
    return self.default_devel()
