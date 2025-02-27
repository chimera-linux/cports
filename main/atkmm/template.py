pkgname = "atkmm"
pkgver = "2.36.3"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "pkgconf"]
makedepends = [
    "at-spi2-core-devel",
    "glibmm-devel",
    "libsigc++-devel",
]
pkgdesc = "C++ accessibility interface bindings"
license = "LGPL-2.1-or-later"
url = "https://www.gtkmm.org"
source = f"$(GNOME_SITE)/atkmm/{pkgver[:-2]}/atkmm-{pkgver}.tar.xz"
sha256 = "6ec264eaa0c4de0adb7202c600170bde9a7fbe4d466bfbe940eaf7faaa6c5974"


@subpackage("atkmm-devel")
def _(self):
    return self.default_devel(
        extra=[
            "usr/lib/atkmm-2.36",
        ]
    )
