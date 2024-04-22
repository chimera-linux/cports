pkgname = "fnott"
pkgver = "1.5.0"
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
sha256 = "0d55adb362d632225e8a1f574ce57f477fba1abac62a3937ddb651de69e4652b"
hardening = ["vis", "cfi"]
# has no tests
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
    self.install_service(self.files_path / "fnott.user")
