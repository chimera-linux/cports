pkgname = "scenefx"
pkgver = "0.5"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "meson",
    "pkgconf",
    "scdoc",
]
makedepends = [
    "json-c-devel",
    "pango-devel",
    "pcre2-devel",
    "wayland-protocols",
    "wlroots0.20-devel",
]
depends = []
pkgdesc = "A drop-in replacement for the wlroots scene API with eye-candy effects"
license = "MIT"
url = "https://github.com/wlrfx/scenefx"
source = f"https://github.com/wlrfx/scenefx/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "0fa8ecca0e310f813efd052624c5ed7d9153d6a0fdead5cc957d34c07f9a86c6"
options = ["!lto"]


def post_install(self):
    self.install_license("LICENSE")


@subpackage("scenefx-devel")
def _(self):
    return self.default_devel()
