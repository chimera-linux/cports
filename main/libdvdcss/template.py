pkgname = "libdvdcss"
pkgver = "1.6.0"
pkgrel = 0
build_style = "meson"
configure_args = ["-Ddefault_library=shared"]
hostmakedepends = ["meson", "ninja", "pkgconf"]
makedepends = ["linux-headers"]
pkgdesc = "Library for accessing DVDs"
license = "GPL-2.0-or-later"
url = "https://www.videolan.org/developers/libdvdcss.html"
source = f"https://download.videolan.org/pub/libdvdcss/{pkgver}/libdvdcss-{pkgver}.tar.xz"
sha256 = "7ea556c846b7bfc32d47b41cae56d1863a6b6d5f706bb162778d6f298490977c"


@subpackage("libdvdcss-devel")
def _(self):
    return self.default_devel()
