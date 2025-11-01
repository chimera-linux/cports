pkgname = "wlroots0.18"
pkgver = "0.18.3"
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
# do not carry over; unversioned names are deprecated
provides = [self.with_pkgver("wlroots")]
pkgdesc = "Modular Wayland compositor library 0.18.x"
license = "MIT"
url = "https://gitlab.freedesktop.org/wlroots/wlroots"
source = f"{url}/-/releases/{pkgver}/downloads/wlroots-{pkgver}.tar.gz"
sha256 = "164a7c8bf9f8ae2c1fb00e7bddb6f08cad7e81b3eb35577b48483b1ac265a087"


def post_install(self):
    self.install_license("LICENSE")


@subpackage("wlroots0.18-devel")
def _(self):
    self.provides = [self.with_pkgver("wlroots-devel")]
    return self.default_devel()
