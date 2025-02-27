pkgname = "libsigc++"
pkgver = "3.6.0"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Dmaintainer-mode=false",
    "-Dbuild-documentation=false",
    "-Dbuild-examples=false",
    "-Dbenchmark=false",
    "-Dwarnings=max",
]
hostmakedepends = ["meson", "pkgconf"]
pkgdesc = "Type-safe callback system for C++"
license = "LGPL-3.0-only"
url = "https://libsigcplusplus.github.io/libsigcplusplus"
source = f"$(GNOME_SITE)/libsigc++/{pkgver[:-2]}/libsigc++-{pkgver}.tar.xz"
sha256 = "c3d23b37dfd6e39f2e09f091b77b1541fbfa17c4f0b6bf5c89baef7229080e17"


@subpackage("libsigc++-devel")
def _(self):
    return self.default_devel(
        extra=[
            "usr/lib/sigc++-3.0",
        ]
    )
