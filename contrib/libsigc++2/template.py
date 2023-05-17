pkgname = "libsigc++2"
pkgver = "2.12.0"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Dbuild-examples=false", "-Dwarnings=max"
]
hostmakedepends = ["meson", "pkgconf"]
pkgdesc = "Type-safe callback system for C++ (2.x)"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://libsigcplusplus.github.io/libsigcplusplus"
source = f"$(GNOME_SITE)/libsigc++/{pkgver[:-2]}/libsigc++-{pkgver}.tar.xz"
sha256 = "1c466d2e64b34f9b118976eb21b138c37ed124d0f61497df2a90ce6c3d9fa3b5"

@subpackage("libsigc++2-devel")
def _devel(self):
    return self.default_devel(extra = [
        "usr/lib/sigc++-2.0",
    ])
