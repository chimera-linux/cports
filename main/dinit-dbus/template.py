pkgname = "dinit-dbus"
pkgver = "0_git20260624"
pkgrel = 0
_gitrev = "5662aa890b08e7daec58942fdaae5b105cb881af"
build_style = "meson"
hostmakedepends = ["meson", "pkgconf"]
makedepends = ["dinit-chimera", "dbus-devel", "libdinitctl-devel"]
checkdepends = ["dbus"]
depends = ["dbus"]
replaces = ["dbus-dinit<1.14.10-r14"]
pkgdesc = "DBus interface to dinit"
license = "BSD-2-Clause"
url = "https://github.com/chimera-linux/dinit-dbus"
source = f"{url}/archive/{_gitrev}.tar.gz"
sha256 = "c6dc3dfa504326867481c38b09fb78353431e9467180646217161cbe0a9f6df3"


def post_install(self):
    self.install_license("COPYING.md")
    self.install_service(self.files_path / "dbus")
    self.install_service(self.files_path / "dbus.user")
    self.install_service(self.files_path / "dinit-dbus")
    self.install_service(self.files_path / "dinit-dbus.user")
