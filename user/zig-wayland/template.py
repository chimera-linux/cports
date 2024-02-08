pkgname = "zig-wayland"
pkgver = "0.2.0"
pkgrel = 0
build_style = "zig_package"
hostmakedepends = ["zig"]
pkgdesc = "Zig bindings for libwayland"
maintainer = "Isaac Freund <mail@isaacfreund.com>"
license = "MIT"
url = "https://codeberg.org/ifreund/zig-wayland"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "831ce41cb0aad8da97de5e27125cbdd80454e5da8fd52aa78e918c0e0c784d70"


def post_install(self):
    self.install_license("LICENSE")
