pkgname = "hyprland"
pkgver = "0.56.2"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DNO_SYSTEMD=ON",
]
hostmakedepends = [
    "cmake",
    "glslang-progs",
    "hyprwayland-scanner",
    "ninja",
    "pkgconf",
    "python",
    "wayland-progs",
]
makedepends = [
    "aquamarine-devel",
    "cairo-devel",
    "glaze",
    "glib-devel",
    "glslang-devel",
    "hyprcursor-devel",
    "hyprgraphics-devel",
    "hyprland-protocols",
    "hyprlang-devel",
    "hyprutils-devel",
    "hyprwire-devel",
    "lcms2-devel",
    "libdrm-devel",
    "libei-devel",
    "libinput-devel",
    "libxcb-devel",
    "libxcursor-devel",
    "libxkbcommon-devel",
    "lua5.5-devel",
    "mesa-devel",
    "mesa-gbm-devel",
    "muparser-devel",
    "pango-devel",
    "pixman-devel",
    "re2-devel",
    "readline-devel",
    "spirv-tools-devel",
    "tomlplusplus-devel",
    "util-linux-uuid-devel",
    "wayland-devel",
    "wayland-protocols",
    "xcb-util-errors-devel",
    "xcb-util-wm-devel",
]
depends = [
    "hyprland-guiutils",
    "xwayland",
]
pkgdesc = "Dynamic tiling Wayland compositor"
license = "BSD-3-Clause"
url = "https://hypr.land"
source = f"https://github.com/hyprwm/Hyprland/releases/download/v{pkgver}/source-v{pkgver}.tar.gz"
sha256 = "03ad3f5ef152ff44116ffd56fcf808486211ecabf4f0ba567108ee746ba5cd2e"


def post_install(self):
    self.install_license("LICENSE")


@subpackage("hyprland-devel")
def _(self):
    return self.default_devel()
