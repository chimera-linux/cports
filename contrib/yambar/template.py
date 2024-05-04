pkgname = "yambar"
pkgver = "1.11.0"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "bison",
    "flex",
    "meson",
    "pkgconf",
    "scdoc"
]
makedepends = [
    "alsa-lib-devel",
    "fcft-devel",
    "json-c-devel",
    "libinput-devel",
    "libmpdclient-devel"
    "libxcb-devel",
    "libyaml-devel",
    "pipewire-devel",
    "pixman-devel",
    "tllist",
    "udev-devel",
    "wayland-devel",
    "wayland-protocols",
    "xcb-util-cursor-devel",
    "xcb-util-devel",
    "xcb-util-wm-devel",
]
pkgdesc = "Modular status panel for X11 and Wayland"
maintainer = "ogromny <ogromnycoding@gmail.com>"
license = "MIT"
url = "https://codeberg.org/dnkl/yambar"
source = f"https://codeberg.org/dnkl/{pkgname}/releases/download/{pkgver}/{pkgname}-{pkgver}.tar.gz"
sha256 = "9859ef16ba16069c3442283d76607712c0b7bc602b6fadf41b2c3d97a754d5f9"


def post_install(self):
    self.install_license("LICENSE")
