pkgname = "fcft"
pkgver = "3.1.8"
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
sha256 = "f48c793f354b8be95477e475dde7c98ac9d2628c52ecb42029dc6d20b52d787c"
hardening = ["vis", "cfi"]


def post_install(self):
    self.rename(
        "usr/share/doc/fcft/LICENSE",
        f"usr/share/licenses/{pkgname}/LICENSE",
        relative=False,
    )


@subpackage("fcft-devel")
def _devel(self):
    return self.default_devel()
