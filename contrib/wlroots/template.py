pkgname = "wlroots"
pkgver = "0.16.2"
pkgrel = 0
build_style = "meson"
configure_args = ["-Dexamples=false", "-Dwerror=false"]
hostmakedepends = [
    "meson",
    "pkgconf",
    "glslang-progs",
    "xwayland",
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
    "vulkan-loader",
    "wayland-devel",
    "wayland-protocols",
    "xcb-util-renderutil-devel",
    "xcb-util-wm-devel",
]
pkgdesc = "Modular Wayland compositor library"
maintainer = "flukey <flukey@vapourmail.eu>"
license = "MIT"
url = "https://gitlab.freedesktop.org/wlroots/wlroots"
source = f"https://gitlab.freedesktop.org/wlroots/wlroots/-/releases/{pkgver}/downloads/{pkgname}-{pkgver}.tar.gz"
sha256 = "83e9a11605f23d4bf781ab1947089483d9ec3f7e9ba65398e0609593b77d44aa"


@subpackage("wlroots-devel")
def _devel(self):
    return self.default_devel()
