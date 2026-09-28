pkgname = "pixman"
pkgver = "0.46.4"
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
sha256 = "d09c44ebc3bd5bee7021c79f922fe8fb2fb57f7320f55e97ff9914d2346a591c"
# needs a lot larger stack than musl default
tool_flags = {"LDFLAGS": ["-Wl,-z,stack-size=2097152"]}
# FIXME int (test fails)
hardening = ["!int"]


def post_install(self):
    self.install_license("COPYING")


@subpackage("pixman-devel")
def _(self):
    return self.default_devel()
