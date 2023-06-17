pkgname = "fcft"
pkgver = "3.1.5"
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
sha256 = "8a7e09c887edce97f8780dba8a060026c3551da48252819400d7af1c5eacf871"
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
