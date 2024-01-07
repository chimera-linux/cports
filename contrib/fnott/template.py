pkgname = "fnott"
pkgver = "1.4.1"
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
pkgdesc = "Keyboard driven wayland notification daemon"
maintainer = "psykose <alice@ayaya.dev>"
license = "MIT"
url = "https://codeberg.org/dnkl/fnott"
source = f"{url}/archive/{pkgver}.tar.gz"
sha256 = "20da05357aa83b3541b6c02bb162af10c89519602bc91fdfaa190239ce303300"
hardening = ["vis", "cfi"]
# has no tests
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
    self.install_service(self.files_path / "fnott.user")
