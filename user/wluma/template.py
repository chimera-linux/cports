pkgname = "wluma"
pkgver = "4.10.0"
pkgrel = 0
build_style = "cargo"
hostmakedepends = [
    "cargo-auditable",
    "pkgconf",
]
makedepends = [
    "dbus-devel",
    "dinit-chimera",
    "linux-headers",
    "turnstile",
    "udev-devel",
    "v4l-utils-devel",
    "vulkan-loader-devel",
]
pkgdesc = "Automatic brightness adjustment based on screen contents and ALS"
license = "ISC"
url = "https://github.com/maximbaz/wluma"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "98bad2ddea87eae15b81d32a452e19b638b9afea14361d67473c45226c6cf0ea"


def post_install(self):
    self.install_license("LICENSE")
    self.install_service("^/wluma.user")
