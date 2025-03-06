pkgname = "fcft"
pkgver = "3.2.0"
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
sha256 = "6d946befcd4edf54d9ae173b8883faa46d84ab554b250f6cb3c659fb8d6b0f71"


def post_install(self):
    self.rename(
        "usr/share/doc/fcft/LICENSE",
        f"usr/share/licenses/{pkgname}/LICENSE",
        relative=False,
    )


@subpackage("fcft-devel")
def _(self):
    return self.default_devel()
