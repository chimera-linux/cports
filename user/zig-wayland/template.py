pkgname = "zig-wayland"
pkgver = "0.1.0"
pkgrel = 0
build_style = "zig_package"
hostmakedepends = ["zig"]
pkgdesc = "Zig bindings for libwayland"
maintainer = "Isaac Freund <mail@isaacfreund.com>"
license = "MIT"
url = "https://codeberg.org/ifreund/zig-wayland"
source = f"{url}/archive/e47e885f5361f7b4d25cc4a7ae856f276b314b34.tar.gz"
sha256 = "46ce978744d2b4e5ba563b220a9a7a320fc1ea7b15b82800825efd685fa7e0af"


def post_install(self):
    self.install_license("LICENSE")
