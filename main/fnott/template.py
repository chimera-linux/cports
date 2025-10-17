pkgname = "fnott"
pkgver = "1.8.0"
pkgrel = 1
build_style = "meson"
hostmakedepends = [
    "meson",
    "pkgconf",
    "scdoc",
    "wayland-devel",
]
makedepends = [
    "dbus-devel",
    "dinit-chimera",
    "dinit-dbus",
    "fcft-devel",
    "linux-headers",
    "pixman-devel",
    "tllist",
    "turnstile",
    "wayland-devel",
    "wayland-protocols",
]
depends = ["dinit-dbus"]
pkgdesc = "Keyboard driven wayland notification daemon"
license = "MIT"
url = "https://codeberg.org/dnkl/fnott"
source = f"{url}/archive/{pkgver}.tar.gz"
sha256 = "7e784133bec7cc197bbeed18daf92192f297f7c60d1c25cce318ae09f70ab0e1"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("LICENSE")
    self.install_service(self.files_path / "fnott.user")
