pkgname = "dinit-userservd"
pkgver = "0.1.0"
_commit = "4427f4614320af3259e1197d7c5be6ade897339b"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "pkgconf"]
makedepends = ["linux-pam-devel"]
pkgdesc = "Dinit user instance manager"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-2-Clause"
url = "https://github.com/chimera-linux/dinit-userservd"
source = f"https://github.com/chimera-linux/{pkgname}/archive/{_commit}.tar.gz"
sha256 = "f7b4b646153aabc8ad865e2b3633dbc04e662b1e9fbb1ef92506e1f81a7e658b"

@subpackage("dinit-userservd-dbus")
def _dbus(self):
    self.pkgdesc = f"{pkgdesc} (dbus session runner)"
    self.depends = ["dbus"]
    self.install_if = [f"{pkgname}={pkgver}-r{pkgrel}", "dbus"]

    return ["usr/bin/dinit-run-dbus"]
