pkgname = "kanshi"
pkgver = "1.6.0"
pkgrel = 0
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
sha256 = "1021bee594672c5304caf548865459bab097f0e2f95de3865ec2079c76a1aaac"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("LICENSE")
    self.install_service(self.files_path / "kanshi.user")
