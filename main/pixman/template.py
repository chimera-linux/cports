pkgname = "pixman"
pkgver = "0.43.2"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Dgnu-inline-asm=enabled",
    "-Dlibpng=enabled",
    "-Dgtk=disabled",
    "-Dopenmp=disabled",
    "-Diwmmxt=disabled",
    "-Da64-neon=disabled",  # added with 0.42.x, fails to build on clang
]
make_check_args = ["--timeout-multiplier", "3"]
hostmakedepends = ["meson", "pkgconf", "perl"]
makedepends = ["linux-headers", "libpng-devel"]
pkgdesc = "Library of low-level pixel manipulation routines"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://pixman.org"
source = f"https://www.cairographics.org/releases/{pkgname}-{pkgver}.tar.gz"
sha256 = "ea79297e5418fb528d0466e8b5b91d1be88857fa3706f49777b2925a72ae9924"
# needs a lot larger stack than musl default
tool_flags = {"LDFLAGS": ["-Wl,-z,stack-size=2097152"]}
# FIXME int (test fails)
hardening = ["!int"]


def post_install(self):
    self.install_license("COPYING")


@subpackage("pixman-devel")
def _devel(self):
    return self.default_devel()
