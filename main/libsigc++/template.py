pkgname = "libsigc++"
pkgver = "3.4.0"
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
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-3.0-only"
url = "https://libsigcplusplus.github.io/libsigcplusplus"
source = f"$(GNOME_SITE)/{pkgname}/{pkgver[:-2]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "02e2630ffb5ce93cd52c38423521dfe7063328863a6e96d41d765a6116b8707e"


@subpackage("libsigc++-devel")
def _devel(self):
    return self.default_devel(
        extra=[
            "usr/lib/sigc++-3.0",
        ]
    )
