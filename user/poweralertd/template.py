pkgname = "poweralertd"
pkgver = "0.3.0"
pkgrel = 1
build_style = "meson"
hostmakedepends = [
    "meson",
    "pkgconf",
    "scdoc",
]
makedepends = ["dinit-chimera", "tangle-devel"]
depends = ["upower"]
pkgdesc = "UPower-powered power alerter"
license = "GPL-3.0-only"
url = "https://sr.ht/~kennylevinsen/poweralertd"
source = f"https://git.sr.ht/~kennylevinsen/poweralertd/archive/{pkgver}.tar.gz"
sha256 = "5b2a1d0fefab62e5ddb5784f2cd3d330f36b3cb5260936f5051f6ff89d8abc3f"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_service(self.files_path / "poweralertd.user")
