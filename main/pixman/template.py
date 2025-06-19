pkgname = "pixman"
pkgver = "0.46.2"
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
license = "MIT"
url = "https://pixman.org"
source = f"https://www.cairographics.org/releases/pixman-{pkgver}.tar.gz"
sha256 = "3e0de5ba6e356916946a3d958192f15505dcab85134771bfeab4ce4e29bbd733"
# needs a lot larger stack than musl default
tool_flags = {"LDFLAGS": ["-Wl,-z,stack-size=2097152"]}
# FIXME int (test fails)
hardening = ["!int"]


def post_install(self):
    self.install_license("COPYING")


@subpackage("pixman-devel")
def _(self):
    return self.default_devel()
