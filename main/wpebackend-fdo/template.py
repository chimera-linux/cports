pkgname = "wpebackend-fdo"
pkgver = "1.12.1"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "pkgconf", "wayland-progs"]
makedepends = ["glib-devel", "libepoxy-devel", "libwpe-devel", "wayland-devel"]
pkgdesc = "Wayland backend for WPE WebKit"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-2-Clause"
url = "https://wpewebkit.org"
source = f"{url}/releases/{pkgname}-{pkgver}.tar.xz"
sha256 = "45aa833c44ec292f31fa943b01b8cc75e54eb623ad7ba6a66fc2f118fe69e629"

def post_install(self):
    self.install_license("COPYING")

@subpackage("wpebackend-fdo-devel")
def _devel(self):
    self.depends += [f"{pkgname}={pkgver}-r{pkgrel}"]
    # does not include the .so file; it's dlopened by things at runtime
    return [
        "usr/include",
        "usr/lib/pkgconfig",
    ]
