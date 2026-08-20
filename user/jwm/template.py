pkgname = "jwm"
pkgver = "2.4.6"
pkgrel = 0
build_style = "gnu_configure"
configure_gen = ["./autogen.sh"]
make_dir = "."
hostmakedepends = [
    "autoconf",
    "automake",
    "pkgconf",
]
makedepends = [
    "cairo-devel",
    "gettext-devel",
    "libjpeg-turbo-devel",
    "libpng-devel",
    "libx11-devel",
    "libxext-devel",
    "libxinerama-devel",
    "libxmu-devel",
    "libxpm-devel",
    "libxrender-devel",
    "pango-devel",
]
depends = ["pango-xft"]
pkgdesc = "Joe's Window Manager"
license = "MIT"
url = "https://github.com/joewing/jwm"
source = f"{url}/releases/download/v{pkgver}/jwm-{pkgver}.tar.xz"
sha256 = "b5871ec28317594b3fa22b83ed5524cc911d498c455eaab3ae68def195dd802d"
# no tests, uses etcfiles for system config
options = ["!check", "etcfiles"]


def post_install(self):
    self.install_license("LICENSE")
