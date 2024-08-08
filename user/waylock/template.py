pkgname = "waylock"
pkgver = "1.2.0"
pkgrel = 0
build_style = "zig_build"
zig_build_args = ["-Dpie", "-Dstrip"]
hostmakedepends = [
    "zig",
    "pkgconf",
    # TODO this should be wayland-progs, not wayland-devel but the
    # wayland-scanner.pc file is in the wrong package
    "wayland-devel",
    "wayland-protocols",
]
makedepends = [
    "libxkbcommon-devel",
    "linux-pam-devel",
    "wayland-devel",
    "zig-wayland",
    "zig-xkbcommon",
]
pkgdesc = "Small screenlocker for Wayland compositors"
maintainer = "Isaac Freund <mail@isaacfreund.com>"
license = "ISC"
url = "https://codeberg.org/ifreund/waylock"
source = f"https://codeberg.org/ifreund/waylock/releases/download/v{pkgver}/waylock-{pkgver}.tar.gz"
sha256 = "343fbb043bea54f5fd93e9fdb3ef441e6bfada60e8bf754d840a20e985689582"


def post_install(self):
    self.install_license("LICENSE")
