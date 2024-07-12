pkgname = "wlroots0.15"
pkgver = "0.15.1"
pkgrel = 0
build_style = "meson"
configure_args = ["-Dexamples=false", "--includedir=/usr/include/wlroots-0.16"]
hostmakedepends = [
    "meson",
    "pkgconf",
    "glslang-progs",
    "xwayland-devel",
]
makedepends = [
    "hwdata-devel",
    "libdrm-devel",
    "libgbm-devel",
    "libinput-devel",
    "libseat-devel",
    "libxcb-devel",
    "libxkbcommon-devel",
    "mesa-devel",
    "pixman-devel",
    "udev-devel",
    "vulkan-headers",
    "vulkan-loader-devel",
    "wayland-devel",
    "wayland-protocols",
    "xcb-util-errors-devel",
    "xcb-util-renderutil-devel",
    "xcb-util-wm-devel",
]
pkgdesc = "Modular Wayland compositor library 0.15.x"
maintainer = "ttyyls <contact@behri.org>"
license = "MIT"
url = "https://gitlab.freedesktop.org/wlroots/wlroots"
source = f"https://gitlab.freedesktop.org/wlroots/wlroots/-/releases/{pkgver}/downloads/wlroots-{pkgver}.tar.gz"
sha256 = "5b92f11a52d978919ed1306e0d54c9d59f1762b28d44f0a2da3ef3b351305373"


def post_install(self):
    self.install_license("LICENSE")


@subpackage("wlroots0.15-devel")
def _devel(self):
    return self.default_devel()
