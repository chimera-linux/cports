pkgname = "dinit-dbus"
pkgver = "0_git20250206"
pkgrel = 0
_gitrev = "95e6e66a504e822e64cf80a59d04eaa44b669f57"
build_style = "meson"
hostmakedepends = ["meson", "pkgconf"]
makedepends = ["dbus-devel", "libdinitctl-devel"]
checkdepends = ["dbus"]
depends = ["dbus"]
replaces = ["dbus-dinit<1.14.10-r14"]
pkgdesc = "DBus interface to dinit"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-2-Clause"
url = "https://github.com/chimera-linux/dinit-dbus"
source = f"{url}/archive/{_gitrev}.tar.gz"
sha256 = "095aaa0da632f2bc1f3b0c2d3a21e4e9e5b3728149b6d31629107c7215d0213c"


def post_install(self):
    self.install_license("COPYING.md")
    self.install_service(self.files_path / "dbus")
    self.install_service(self.files_path / "dbus.user")
    self.install_service(self.files_path / "dinit-dbus")
    self.install_service(self.files_path / "dinit-dbus.user")
