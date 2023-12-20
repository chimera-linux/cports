pkgname = "yambar"
pkgver = "1.10.0"
pkgrel = 0
build_style = "meson"
make_check_wrapper = ["weston-headless-run"]
hostmakedepends = ["bison", "flex", "meson", "pkgconf", "scdoc"]
makedepends = [
    "alsa-lib-devel",
    "fcft-devel",
    "json-c-devel",
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
checkdepends = ["weston", "fonts-liberation-ttf"]
pkgdesc = "Modular status panel for X11 and Wayland"
maintainer = "triallax <triallax@tutanota.com>"
license = "MIT"
url = "https://codeberg.org/dnkl/yambar"
source = f"https://codeberg.org/dnkl/yambar/archive/{pkgver}.tar.gz"
sha256 = "3c53d6fc245707d6ff6174395b03d7f069a48da9fb63b612c82d706c1c09b193"


def post_install(self):
    self.install_license("LICENSE")
