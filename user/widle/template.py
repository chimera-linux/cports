pkgname = "widle"
pkgver = "1.0"
pkgrel = 0
build_style = "makefile"
hostmakedepends = [
    "pkgconf",
    "wayland-progs",
]
makedepends = [
    "wayland-devel",
    "wayland-protocols",
]
pkgdesc = "Run a command upon becoming idle"
license = "MIT"
url = "https://codeberg.org/sewn/widle"
source = f"{url}/archive/{pkgver}.tar.gz"
sha256 = "729f37e232d0863d33486641ac874c72d005a9e27d226110cc65ddbbe1ef00fa"
# no test suite
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
