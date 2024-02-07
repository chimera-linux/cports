pkgname = "zig-wayland"
pkgver = "0.2.0"
pkgrel = 0
pkgdesc = "Zig bindings for libwayland"
maintainer = "Isaac Freund <mail@isaacfreund.com>"
license = "MIT"
url = "https://codeberg.org/ifreund/zig-wayland"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "831ce41cb0aad8da97de5e27125cbdd80454e5da8fd52aa78e918c0e0c784d70"


def do_install(self):
    self.install_files(
        ".",
        "usr/src/zig/packages/",
        name="122062beeb6fd2bb21c91e81acb3ea6cbba69d3c00a31b62732254e190b5fc7a934e",
    )


def post_install(self):
    self.install_license("LICENSE")
