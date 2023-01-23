pkgname = "libsigc++"
pkgver = "3.2.0"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Dmaintainer-mode=false", "-Dbuild-documentation=false",
    "-Dbuild-examples=false", "-Dbenchmark=false", "-Dwarnings=max"
]
hostmakedepends = ["meson", "pkgconf"]
pkgdesc = "Type-safe callback system for C++"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-3.0-only"
url = "https://libsigcplusplus.github.io/libsigcplusplus"
source = f"$(GNOME_SITE)/{pkgname}/{pkgver[:-2]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "8cdcb986e3f0a7c5b4474aa3c833d676e62469509f4899110ddf118f04082651"

@subpackage("libsigc++-devel")
def _devel(self):
    return self.default_devel(extra = [
        "usr/lib/sigc++-3.0",
    ])
