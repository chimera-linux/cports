pkgname = "kanshi"
pkgver = "1.8.0"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "meson",
    "pkgconf",
    "scdoc",
]
makedepends = [
    "dinit-chimera",
    "libscfg-devel",
    "turnstile",
    "varlink-devel",
    "wayland-devel",
]
pkgdesc = "Dynamic display configuration for wayland"
license = "MIT"
url = "https://gitlab.freedesktop.org/emersion/kanshi"
source = f"{url}/-/archive/v{pkgver}/kanshi-{pkgver}.tar.gz"
sha256 = "4b2c004c6adfa181b1e8f68de216d9b71f449727ae2712226302c14972230030"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("LICENSE")
    self.install_service(self.files_path / "kanshi.user")
