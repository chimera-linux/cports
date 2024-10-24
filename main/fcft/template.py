pkgname = "fcft"
pkgver = "3.1.9"
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
sha256 = "4b7e3b2ab7e14f532d8a9cb0f2d3b0cdf9d2919b95e6ab8030f7ac87d059c2b6"
hardening = ["vis", "cfi"]


def post_install(self):
    self.rename(
        "usr/share/doc/fcft/LICENSE",
        f"usr/share/licenses/{pkgname}/LICENSE",
        relative=False,
    )


@subpackage("fcft-devel")
def _(self):
    return self.default_devel()
