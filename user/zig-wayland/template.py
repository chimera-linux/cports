pkgname = "zig-wayland"
pkgver = "0.1.0"
pkgrel = 0
pkgdesc = "Zig bindings for libwayland"
maintainer = "Isaac Freund <mail@isaacfreund.com>"
license = "MIT"
url = "https://codeberg.org/ifreund/zig-wayland"
source = f"{url}/archive/e47e885f5361f7b4d25cc4a7ae856f276b314b34.tar.gz"
sha256 = "46ce978744d2b4e5ba563b220a9a7a320fc1ea7b15b82800825efd685fa7e0af"


def do_install(self):
    self.install_files(
        ".",
        "usr/src/zig/packages/",
        name="122062beeb6fd2bb21c91e81acb3ea6cbba69d3c00a31b62732254e190b5fc7a934e",
    )


def post_install(self):
    self.install_license("LICENSE")
