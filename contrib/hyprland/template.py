pkgname = "hyprland"
pkgver = "0.29.1"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "cmake",
    "git",
    "jq",
    "meson",
    "ninja",
    "pkgconf"
]
makedepends = [
    "cairo-devel",
    "hwdata-devel",
    "libavcodec",
    "libavformat",
    "libavutil",
    "libdisplay-info-devel",
    "libdrm-devel",
    "libgbm-devel",
    "libgles2",
    "libinput-devel",
    "libliftoff-devel",
    "libpng-devel",
    "libseat-devel",
    "libxcb-devel",
    "libxfixes-devel",
    "libxkbcommon-devel",
    "mesa-devel",
    "pango-devel",
    "pixman-devel",
    "udev-devel",
    "wayland-devel",
    "wayland-protocols"
]
pkgdesc = "Customizable wayland compositor that doesn't sacrifice on looks"
maintainer = "Froggo <froggo8311@proton.me>"
license = "BSD-3-Clause"
url = "https://hyprland.org"
source = f"https://github.com/hyprwm/Hyprland/releases/download/v{pkgver}/source-v{pkgver}.tar.gz"
sha256 = "5af3ba19c17466085f4458882a342090327ca400177aac3017aa8ccff34859d0"

def post_install(self):
    self.install_license("LICENSE")

@subpackage("hyprland-devel")
def _devel(self):
    return self.default_devel()
