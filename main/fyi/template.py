pkgname = "fyi"
pkgver = "1.0.4"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "meson",
    "pkgconf",
]
makedepends = ["dbus-devel"]
pkgdesc = "Desktop notification sending utility"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "MIT"
url = "https://codeberg.org/dnkl/fyi"
source = f"{url}/archive/{pkgver}.tar.gz"
sha256 = "6d196b4725df02dba39ca736c0f5b485f6a204a98f68de6bbe8155bdc1e56d24"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("LICENSE")
