pkgname = "wlroots0.18"
pkgver = "0.18.2"
pkgrel = 0
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
provides = [self.with_pkgver("wlroots")]
pkgdesc = "Modular Wayland compositor library 0.18.x"
maintainer = "flukey <flukey@vapourmail.eu>"
license = "MIT"
url = "https://gitlab.freedesktop.org/wlroots/wlroots"
source = f"{url}/-/releases/{pkgver}/downloads/wlroots-{pkgver}.tar.gz"
sha256 = "cf776c169169f279808d9eabc6583f484338dcd454c966a285ff178c88c105d4"


def post_install(self):
    self.install_license("LICENSE")


@subpackage("wlroots0.18-devel")
def _(self):
    self.provides = [self.with_pkgver("wlroots-devel")]
    return self.default_devel()
