pkgname = "pixman"
pkgver = "0.44.2"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Dgnu-inline-asm=enabled",
    "-Dlibpng=enabled",
    "-Dgtk=disabled",
    "-Dopenmp=disabled",
]
make_check_args = ["--timeout-multiplier", "3"]
hostmakedepends = ["meson", "pkgconf", "perl"]
makedepends = ["linux-headers", "libpng-devel"]
pkgdesc = "Library of low-level pixel manipulation routines"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://pixman.org"
source = f"https://www.cairographics.org/releases/pixman-{pkgver}.tar.gz"
sha256 = "6349061ce1a338ab6952b92194d1b0377472244208d47ff25bef86fc71973466"
# needs a lot larger stack than musl default
tool_flags = {"LDFLAGS": ["-Wl,-z,stack-size=2097152"]}
# FIXME int (test fails)
hardening = ["!int"]


def post_install(self):
    self.install_license("COPYING")


@subpackage("pixman-devel")
def _(self):
    return self.default_devel()
