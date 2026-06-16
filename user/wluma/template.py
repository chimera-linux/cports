pkgname = "wluma"
pkgver = "4.11.1"
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
sha256 = "1b66145af53bbfc437e4314fe27f776cb73c5cb8c7893bf1c008b9a81532b710"


def post_install(self):
    self.install_license("LICENSE")
    self.install_service("^/wluma.user")
