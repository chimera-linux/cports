pkgname = "libdvdread"
pkgver = "7.1.1"
pkgrel = 0
build_style = "meson"
configure_args = ["-Ddefault_library=shared", "-Dlibdvdcss=enabled"]
hostmakedepends = ["meson", "ninja", "pkgconf"]
makedepends = ["libdvdcss-devel"]
pkgdesc = "DVD access library"
license = "GPL-2.0-or-later"
url = "https://www.videolan.org/developers/libdvdread.html"
source = f"https://download.videolan.org/pub/videolan/libdvdread/{pkgver}/libdvdread-{pkgver}.tar.xz"
sha256 = "a0d47876548bec806774bbf8dbf20bb19ba139464383156b32eb8e59915b90a9"


@subpackage("libdvdread-devel")
def _(self):
    return self.default_devel()
