pkgname = "kanshi"
pkgver = "1.9.0"
pkgrel = 1
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
    "vali-devel",
    "wayland-devel",
]
pkgdesc = "Dynamic display configuration for wayland"
license = "MIT"
url = "https://gitlab.freedesktop.org/emersion/kanshi"
source = f"{url}/-/archive/v{pkgver}/kanshi-{pkgver}.tar.gz"
sha256 = "048837a6ab79ff430b0ac2586890f03dc5265d7949c010bd9711532caafd66ec"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("LICENSE")
    self.install_service(self.files_path / "kanshi.user")
