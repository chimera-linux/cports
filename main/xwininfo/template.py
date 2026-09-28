pkgname = "xwininfo"
pkgver = "1.1.7"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["automake", "gettext-devel", "pkgconf", "xorg-util-macros"]
makedepends = ["libx11-devel"]
pkgdesc = "Query information about X windows"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/app/xwininfo-{pkgver}.tar.gz"
sha256 = "5484f0059a8ffab6f9493cc9f508735ebb4f0ae801fe759dd270ccb4b7f11d29"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("COPYING")
