pkgname = "hyprtoolkit"
pkgver = "0.5.4"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DOPENGL_opengl_LIBRARY=/usr/lib/libGL.so",
]
hostmakedepends = [
    "cmake",
    "hyprwayland-scanner",
    "ninja",
    "pkgconf",
    "wayland-progs",
]
makedepends = [
    "aquamarine-devel",
    "cairo-devel",
    "hyprgraphics-devel",
    "hyprlang-devel",
    "hyprutils-devel",
    "iniparser-devel",
    "libdrm-devel",
    "libxkbcommon-devel",
    "mesa-devel",
    "pango-devel",
    "pixman-devel",
    "wayland-devel",
    "wayland-protocols",
]
pkgdesc = "Modern C++ Wayland-native GUI toolkit"
license = "BSD-3-Clause"
url = "https://github.com/hyprwm/hyprtoolkit"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "2fb59789f231c1c4e9154ceffc1e7524c0cae154807c0d57e6166806255b570f"


def post_install(self):
    self.install_license("LICENSE")


@subpackage("hyprtoolkit-devel")
def _(self):
    return self.default_devel()
