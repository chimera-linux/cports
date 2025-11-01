pkgname = "wlroots0.17"
pkgver = "0.17.4"
pkgrel = 3
build_style = "meson"
configure_args = [
    # all auto features are needed,
    # don't accidentally end up with them disabled
    "--auto-features=enabled",
    "--includedir=/usr/include/wlroots-0.17",
    "-Dexamples=false",
]
hostmakedepends = [
    "glslang-progs",
    "meson",
    "pkgconf",
    "xwayland-devel",
]
makedepends = [
    "hwdata-devel",
    "libdisplay-info-devel",
    "libdrm-devel",
    "libinput-devel",
    "libliftoff-devel",
    "libseat-devel",
    "libxcb-devel",
    "libxkbcommon-devel",
    "mesa-devel",
    "mesa-gbm-devel",
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
pkgdesc = "Modular Wayland compositor library 0.17.x"
license = "MIT"
url = "https://gitlab.freedesktop.org/wlroots/wlroots"
source = f"https://gitlab.freedesktop.org/wlroots/wlroots/-/releases/{pkgver}/downloads/wlroots-{pkgver}.tar.gz"
sha256 = "d3190d19d03446955e68a92c77d4c74af78384b0db39a85a0b1582adc80f36d1"


def post_install(self):
    self.install_license("LICENSE")


@subpackage("wlroots0.17-devel")
def _(self):
    return self.default_devel()
