pkgname = "fnott"
pkgver = "1.7.0"
pkgrel = 2
build_style = "meson"
hostmakedepends = [
    "meson",
    "pkgconf",
    "scdoc",
    "wayland-devel",
]
makedepends = [
    "dbus-devel",
    "fcft-devel",
    "linux-headers",
    "pixman-devel",
    "tllist",
    "wayland-devel",
    "wayland-protocols",
]
depends = ["dinit-dbus"]
pkgdesc = "Keyboard driven wayland notification daemon"
maintainer = "psykose <alice@ayaya.dev>"
license = "MIT"
url = "https://codeberg.org/dnkl/fnott"
source = f"{url}/archive/{pkgver}.tar.gz"
sha256 = "40013d64423332a53aa943b7d9366f25e8cdd3313345f7a74b53c5d33eb49c80"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("LICENSE")
    self.install_service(self.files_path / "fnott.user")
