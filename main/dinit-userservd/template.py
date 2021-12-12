pkgname = "dinit-userservd"
pkgver = "0.1.0"
_commit = "0c8198d51076b7f32eff601efbccd71279b9eacc"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "pkgconf"]
makedepends = ["linux-pam-devel"]
pkgdesc = "Dinit user instance manager"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-2-Clause"
url = "https://github.com/chimera-linux/dinit-userservd"
source = f"https://github.com/chimera-linux/{pkgname}/archive/{_commit}.tar.gz"
sha256 = "dfc9d24a15db9b0a159a6c79c78df93480708995f1b289fd503829295c9ba555"

@subpackage("dinit-userservd-dbus")
def _dbus(self):
    self.pkgdesc = f"{pkgdesc} (dbus session runner)"
    self.depends = ["dbus"]
    self.install_if = [f"{pkgname}={pkgver}-r{pkgrel}", "dbus"]

    return ["usr/bin/dinit-run-dbus"]
