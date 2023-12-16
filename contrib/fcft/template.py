pkgname = "fcft"
pkgver = "3.1.7"
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
sha256 = "53ad699d388812ec210a50ed34114d6a2de40d6fcae5b8bf2b4098d8d4ba7507"
hardening = ["vis", "cfi"]


def post_install(self):
    ded = self.destdir
    self.install_dir(f"usr/share/licenses/{pkgname}")
    self.mv(
        ded / "usr/share/doc/fcft/LICENSE",
        ded / f"usr/share/licenses/{pkgname}/LICENSE",
    )


@subpackage("fcft-devel")
def _devel(self):
    return self.default_devel()
