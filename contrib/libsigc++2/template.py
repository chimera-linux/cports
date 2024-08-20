pkgname = "libsigc++2"
pkgver = "2.12.1"
pkgrel = 0
build_style = "meson"
configure_args = ["-Dbuild-examples=false", "-Dwarnings=max"]
hostmakedepends = ["meson", "pkgconf"]
pkgdesc = "Type-safe callback system for C++, version 2.x"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://libsigcplusplus.github.io/libsigcplusplus"
source = f"$(GNOME_SITE)/libsigc++/{pkgver[:-2]}/libsigc++-{pkgver}.tar.xz"
sha256 = "a9dbee323351d109b7aee074a9cb89ca3e7bcf8ad8edef1851f4cf359bd50843"


@subpackage("libsigc++2-devel")
def _(self):
    return self.default_devel(
        extra=[
            "usr/lib/sigc++-2.0",
        ]
    )
