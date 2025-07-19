pkgname = "fcft"
pkgver = "3.3.2"
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
license = "MIT"
url = "https://codeberg.org/dnkl/fcft"
source = f"{url}/archive/{pkgver}.tar.gz"
sha256 = "79e52aaafc0b57fa2b68ed6127de13e98318050399a939691b8ca30d44d48591"


def post_install(self):
    self.rename(
        "usr/share/doc/fcft/LICENSE",
        f"usr/share/licenses/{pkgname}/LICENSE",
        relative=False,
    )


@subpackage("fcft-devel")
def _(self):
    return self.default_devel()
