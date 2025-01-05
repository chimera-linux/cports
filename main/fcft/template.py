pkgname = "fcft"
pkgver = "3.1.10"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "pkgconf", "scdoc"]
makedepends = [
    "fontconfig-devel",
    "freetype-devel",
    "harfbuzz-devel",
    "pixman-devel",
    "tllist",
    "utf8proc-devel",
]
pkgdesc = "Simple library for font loading and glyph rasterization"
maintainer = "flukey <flukey@vapourmail.eu>"
license = "MIT"
url = "https://codeberg.org/dnkl/fcft"
source = f"{url}/archive/{pkgver}.tar.gz"
sha256 = "4f4807d708f3a195e9a3caaa1ff9171b678af63a7af1c470a8984d601a4514de"


def post_install(self):
    self.rename(
        "usr/share/doc/fcft/LICENSE",
        f"usr/share/licenses/{pkgname}/LICENSE",
        relative=False,
    )


@subpackage("fcft-devel")
def _(self):
    return self.default_devel()
