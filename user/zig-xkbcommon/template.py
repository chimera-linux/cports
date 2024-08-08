pkgname = "zig-xkbcommon"
pkgver = "0.2.0"
pkgrel = 0
build_style = "zig_package"
hostmakedepends = ["zig"]
pkgdesc = "Zig bindings for xkbcommon"
maintainer = "Isaac Freund <mail@isaacfreund.com>"
license = "MIT"
url = "https://codeberg.org/ifreund/zig-xkbcommon"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "7f9a04254e62daa795377181ae741cab31090a2393ee5e1a93b190ea0c39707d"


def post_install(self):
    self.install_license("LICENSE")
