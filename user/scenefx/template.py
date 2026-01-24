pkgname = "scenefx"
pkgver = "0.4.1"
pkgrel = 0
build_style = "meson"

hostmakedepends = [
    "meson",
    "pkgconf",
    "wayland-progs",
    "wayland-protocols",
]

makedepends = [
    "libdrm-devel",
    "libinput-devel",
    "libxkbcommon-devel",
    "mesa-devel",
    "pixman-devel",
    "wayland-devel",
    "wayland-protocols",
    "wlroots0.19-devel",
]

pkgdesc = "Drop-in replacement for the wlroots scene API with eye candy"
license = "MIT"
url = "https://github.com/wlrfx/scenefx"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "fa23f6ff509168d4a5eb0c5a7ef3b8cf3d39e3fba18320c28256e6c91c85d9ff"


def post_install(self):
    self.install_license("LICENSE")


@subpackage("scenefx-devel")
def _(self):
    self.depends = [self.parent]
    return self.default_devel()
