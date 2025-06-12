pkgname = "wlogout"
pkgver = "1.2.2"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "meson",
    "pkgconf",
    "scdoc",
]
makedepends = [
    "gtk+3-devel",
    "gtk-layer-shell-devel",
]
pkgdesc = "Wayland logout menu"
license = "MIT"
url = "https://github.com/ArtsyMacaw/wlogout"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "4c9204bfa19c73f51176c94c67711f54f3e393301c0809c61ae379054060fa46"


def post_install(self):
    self.install_license("LICENSE")
