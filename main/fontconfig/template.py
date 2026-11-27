pkgname = "fontconfig"
pkgver = "2.18.4"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--enable-static",
    "--enable-docs",
    f"--with-cache-dir=/var/cache/{pkgname}",
]
hostmakedepends = [
    "automake",
    "gettext-devel",
    "gperf",
    "libtool",
    "pkgconf",
    "python",
]
makedepends = ["libexpat-devel", "freetype-bootstrap", "util-linux-uuid-devel"]
triggers = ["/usr/share/fonts/*"]
pkgdesc = "Library for configuring and customizing font access"
license = "MIT"
url = "https://www.fontconfig.org"
source = f"https://gitlab.freedesktop.org/api/v4/projects/890/packages/generic/fontconfig/{pkgver}/fontconfig-{pkgver}.tar.xz"
sha256 = "95013637eff5f81d4871dd16cd098c273264c16d0f9f0b27cc43b81b2794bee3"
options = ["etcfiles"]


def post_install(self):
    self.install_license("COPYING")


@split("devel")
def _(self):
    return self.default_devel()
