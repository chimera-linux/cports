pkgname = "mkfontscale"
pkgver = "1.2.4"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--with-bzip2"]
hostmakedepends = ["automake", "pkgconf", "xorg-util-macros"]
makedepends = [
    "bzip2-devel",
    "freetype-devel",
    "libfontenc-devel",
    "xorgproto",
    "zlib-ng-compat-devel",
]
triggers = ["/usr/share/fonts/*"]
pkgdesc = "X11 scalable font index generator"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/app/mkfontscale-{pkgver}.tar.gz"
sha256 = "076cedba00195e81d055fb39eff94c057f97326ac2403cf71460fc613cd200bf"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("COPYING")
