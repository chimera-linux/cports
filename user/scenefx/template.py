pkgname = "scenefx"
pkgver = "0.5"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "glslang-progs",
    "meson",
    "pkgconf",
]
makedepends = [
    "libdrm-devel",
    "libglvnd-devel",
    "libxkbcommon-devel",
    "mesa-gbm-devel",
    "pixman-devel",
    "wayland-devel",
    "wayland-protocols",
    "wlroots0.20-devel",
]
pkgdesc = "Wlroots scene API replacement with effects for wayland compositors"
license = "MIT"
url = "https://github.com/wlrfx/scenefx"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "0fa8ecca0e310f813efd052624c5ed7d9153d6a0fdead5cc957d34c07f9a86c6"


def post_install(self):
    self.install_license("LICENSE")


@subpackage("scenefx-devel")
def _(self):
    self.depends += [self.parent]
    return self.default_devel()
