pkgname = "wlroots0.19"
pkgver = "0.19.0"
pkgrel = 2
build_style = "meson"
configure_args = [
    # all auto features are needed,
    # don't accidentally end up with them disabled
    "--auto-features=enabled",
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
    "lcms2-devel",
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
pkgdesc = "Modular Wayland compositor library 0.19.x"
license = "MIT"
url = "https://gitlab.freedesktop.org/wlroots/wlroots"
source = f"{url}/-/releases/{pkgver}/downloads/wlroots-{pkgver}.tar.gz"
sha256 = "aefb0fe2633b0aad1d66123b2f41afab004fb625e2a7790492cdd39a805cac91"


def post_install(self):
    self.install_license("LICENSE")


@subpackage("wlroots0.19-devel")
def _(self):
    return self.default_devel()
