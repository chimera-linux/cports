pkgname = "tllist"
pkgver = "1.1.0"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "pkgconf"]
pkgdesc = "C header file only implementation of a typed linked list"
maintainer = "flukey <flukey@vapourmail.eu>"
license = "MIT"
url = "https://codeberg.org/dnkl/tllist"
source = f"{url}/archive/{pkgver}.tar.gz"
sha256 = "0e7b7094a02550dd80b7243bcffc3671550b0f1d8ba625e4dff52517827d5d23"
hardening = ["vis", "cfi"]


def post_install(self):
    self.rename(
        "usr/share/doc/tllist/LICENSE",
        f"usr/share/licenses/{pkgname}/LICENSE",
        relative=False,
    )
