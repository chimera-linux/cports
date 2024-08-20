pkgname = "libpst"
pkgver = "0.6.76"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--enable-libpst-shared", "--disable-python"]
hostmakedepends = ["automake", "gettext-devel", "libtool", "pkgconf"]
makedepends = ["libgsf-devel", "zlib-ng-compat-devel"]
pkgdesc = "Library for working with PST files"
maintainer = "triallax <triallax@tutanota.com>"
license = "GPL-2.0-or-later"
url = "https://www.five-ten-sg.com/libpst"
source = f"{url}/packages/libpst-{pkgver}.tar.gz"
sha256 = "3d291beebbdb48d2b934608bc06195b641da63d2a8f5e0d386f2e9d6d05a0b42"
hardening = ["!vis", "!cfi"]


@subpackage("libpst-devel")
def _(self):
    return self.default_devel()


@subpackage("libpst-progs")
def _(self):
    return self.default_progs()
