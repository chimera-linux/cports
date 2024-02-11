pkgname = "kanshi"
pkgver = "1.5.1"
pkgrel = 1
build_style = "meson"
hostmakedepends = [
    "meson",
    "pkgconf",
    "scdoc",
]
makedepends = [
    "varlink-devel",
    "wayland-devel",
]
pkgdesc = "Dynamic display configuration for wayland"
maintainer = "psykose <alice@ayaya.dev>"
license = "MIT"
url = "https://sr.ht/~emersion/kanshi"
source = f"https://git.sr.ht/~emersion/kanshi/archive/v{pkgver}.tar.gz"
sha256 = "d403d2a99170261baa6606336724bc9721f779dc39294d2e088745d7bd41f427"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("LICENSE")
    self.install_service(self.files_path / "kanshi.user")
