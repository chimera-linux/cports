pkgname = "kanshi"
pkgver = "1.7.0"
pkgrel = 2
build_style = "meson"
hostmakedepends = [
    "meson",
    "pkgconf",
    "scdoc",
]
makedepends = [
    "libscfg-devel",
    "varlink-devel",
    "wayland-devel",
]
pkgdesc = "Dynamic display configuration for wayland"
maintainer = "psykose <alice@ayaya.dev>"
license = "MIT"
url = "https://sr.ht/~emersion/kanshi"
source = f"https://git.sr.ht/~emersion/kanshi/archive/v{pkgver}.tar.gz"
sha256 = "d35b2a0b41a36cc55066320ae7ae5b176450546a4ed67ee09e7241ecd36bfc73"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("LICENSE")
    self.install_service(self.files_path / "kanshi.user")
