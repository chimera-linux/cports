pkgname = "libdvdnav"
pkgver = "7.0.0"
pkgrel = 0
build_style = "meson"
configure_args = ["-Ddefault_library=shared"]
hostmakedepends = ["meson", "ninja", "pkgconf"]
makedepends = ["libdvdcss-devel", "libdvdread-devel"]
pkgdesc = "DVD navigation library"
license = "GPL-2.0-or-later"
url = "https://www.videolan.org/developers/libdvdnav.html"
source = f"https://download.videolan.org/pub/videolan/libdvdnav/{pkgver}/libdvdnav-{pkgver}.tar.xz"
sha256 = "a2a18f5ad36d133c74bf9106b6445806fa253b09141a46392550394b647b221e"


@subpackage("libdvdnav-devel")
def _(self):
    return self.default_devel()
