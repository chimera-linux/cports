pkgname = "wev"
pkgver = "1.0.0"
pkgrel = 0
build_style = "makefile"
make_cmd = "gmake"
hostmakedepends = ["gmake", "pkgconf", "scdoc", "wayland-progs"]
makedepends = [
    "libxkbcommon-devel",
    "linux-headers",
    "wayland-devel",
    "wayland-protocols",
]
pkgdesc = "Wayland event viewer"
maintainer = "triallax <triallax@tutanota.com>"
license = "MIT"
url = "https://git.sr.ht/~sircmpwn/wev"
source = f"{url}/archive/{pkgver}.tar.gz"
sha256 = "613a1df1a4879d50ce72023de14aaf05be2e6f51346e84a69f50fc6d8502bbf4"
hardening = ["vis", "cfi"]
# No tests
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
