pkgname = "libxrandr"
pkgver = "1.5.5"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--enable-malloc0returnsnull"]
hostmakedepends = ["automake", "libtool", "pkgconf", "xorg-util-macros"]
makedepends = ["xorgproto", "libxext-devel", "libxrender-devel"]
pkgdesc = "X RandR Library from X.org"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/lib/libXrandr-{pkgver}.tar.gz"
sha256 = "23faedab4675890ba579b8103399132a139527306b18b500c6fe28e090e2a056"


def post_install(self):
    self.install_license("COPYING")


@subpackage("libxrandr-devel")
def _(self):
    return self.default_devel()
