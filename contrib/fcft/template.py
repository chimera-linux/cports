pkgname = "fcft"
pkgver = "3.1.6"
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
sha256 = "904f40d749d198d97c46c5a459cd3c53fe92f008cf1e3e61949f6cf3036a78b7"
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
