pkgname = "aquamarine"
pkgver = "0.14.0"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DOPENGL_opengl_LIBRARY=/usr/lib/libGL.so",
]
make_check_args = [
    "-E",
    "simpleWindow",
]
hostmakedepends = [
    "cmake",
    "hyprwayland-scanner",
    "ninja",
    "pkgconf",
    "wayland-progs",
]
makedepends = [
    "hwdata-devel",
    "hyprutils-devel",
    "libdisplay-info-devel",
    "libdrm-devel",
    "libinput-devel",
    "libseat-devel",
    "mesa-devel",
    "pixman-devel",
    "udev-devel",
    "wayland-devel",
    "wayland-protocols",
]
pkgdesc = "Lightweight rendering backend library"
license = "BSD-3-Clause"
url = "https://github.com/hyprwm/aquamarine"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "5dcf0b17f7dd51539fd7e79d68484f04240b3b63cf9f5f21d5b6dea0088168f9"


def post_install(self):
    self.install_license("LICENSE")


@subpackage("aquamarine-devel")
def _(self):
    return self.default_devel()
