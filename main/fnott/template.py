pkgname = "fnott"
pkgver = "1.7.1"
pkgrel = 0
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
maintainer = "ttyyls <contact@behri.org>"
license = "MIT"
url = "https://codeberg.org/dnkl/fnott"
source = f"{url}/archive/{pkgver}.tar.gz"
sha256 = "39c732f2ac57d18f24ef9112524d71090e2b68b72a892f4a44f3a77a1f067487"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("LICENSE")
    self.install_service(self.files_path / "fnott.user")
