pkgname = "wlroots0.17"
pkgver = "0.17.3"
pkgrel = 1
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
    "libgbm-devel",
    "libinput-devel",
    "libliftoff-devel",
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
provides = [f"wlroots={pkgver}-r{pkgrel}"]
pkgdesc = "Modular Wayland compositor library (0.17.x)"
maintainer = "flukey <flukey@vapourmail.eu>"
license = "MIT"
url = "https://gitlab.freedesktop.org/wlroots/wlroots"
source = f"https://gitlab.freedesktop.org/wlroots/wlroots/-/releases/{pkgver}/downloads/wlroots-{pkgver}.tar.gz"
sha256 = "04d31521bd2b737541b9680098e55ebaaf956e68d692f80479f4ee1236606d98"


def post_install(self):
    self.install_license("LICENSE")


@subpackage("wlroots0.17-devel")
def _devel(self):
    self.provides = [f"wlroots-devel={pkgver}-r{pkgrel}"]
    return self.default_devel()
