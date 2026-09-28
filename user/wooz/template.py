pkgname = "wooz"
pkgver = "0.1.0"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "meson",
    "pkgconf",
]
makedepends = [
    "linux-headers",
    "wayland-devel",
    "wayland-protocols",
]
pkgdesc = "Wayland magnifier"
license = "MIT"
url = "https://github.com/negrel/wooz"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "ebd62375eb74ea238663052d4540ea36479f794efd271801e4ec7f260d06aa47"


def post_install(self):
    self.install_license("LICENSE")
