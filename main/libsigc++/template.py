pkgname = "libsigc++"
pkgver = "3.0.7"
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
sha256 = "bfbe91c0d094ea6bbc6cbd3909b7d98c6561eea8b6d9c0c25add906a6e83d733"

@subpackage("libsigc++-devel")
def _devel(self):
    return self.default_devel(extra = [
        "usr/lib/sigc++-3.0",
    ])
