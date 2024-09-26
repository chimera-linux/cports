pkgname = "wlroots0.16"
pkgver = "0.16.2"
pkgrel = 3
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
pkgdesc = "Modular Wayland compositor library 0.16.x"
maintainer = "flukey <flukey@vapourmail.eu>"
license = "MIT"
url = "https://gitlab.freedesktop.org/wlroots/wlroots"
source = f"https://gitlab.freedesktop.org/wlroots/wlroots/-/releases/{pkgver}/downloads/wlroots-{pkgver}.tar.gz"
sha256 = "83e9a11605f23d4bf781ab1947089483d9ec3f7e9ba65398e0609593b77d44aa"


def post_install(self):
    self.install_license("LICENSE")


@subpackage("wlroots0.16-devel")
def _(self):
    return self.default_devel()
