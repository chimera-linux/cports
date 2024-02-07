pkgname = "waylock"
pkgver = "0.7.0"
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
source = f"https://codeberg.org/ifreund/waylock/archive/0c7643f3c068a7f1e065b16ac1b0094ef16fc3f4.tar.gz"
sha256 = "bd430db84bed4a62ba1d717295008a5cc0f2add7db72a40e9fd95cdaeea937f5"


def post_install(self):
    self.install_license("LICENSE")
