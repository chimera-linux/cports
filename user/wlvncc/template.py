pkgname = "wlvncc"
pkgver = "0_git20250307"
_rev = "bec7a54fbb835824ac6f8cefbf50181189a5c510"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "pkgconf", "wayland-progs"]
makedepends = [
    "aml-devel",
    "ffmpeg-devel",
    "libdrm-devel",
    "libjpeg-turbo-devel",
    "libpng-devel",
    "libxkbcommon-devel",
    "lzo-devel",
    "mesa-devel",
    "openssl3-devel",
    "pixman-devel",
    "wayland-devel",
    "wayland-protocols",
    "zlib-ng-compat-devel",
]
pkgdesc = "Wayland native vnc client"
license = "ISC AND GPL-2.0-or-later"
url = "https://github.com/any1/wlvncc"
source = f"{url}/archive/{_rev}.tar.gz"
sha256 = "81d9d4549779494ca10f90e54d0ff01a1fb0cef5009fd3fe9bfb508bbe6ac244"


def post_install(self):
    self.install_license("COPYING")
