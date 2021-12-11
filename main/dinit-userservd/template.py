pkgname = "dinit-userservd"
pkgver = "0.1.0"
_commit = "1ca314f6aac5681b2fa5e70c3a180b6644cc09b5"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "pkgconf"]
makedepends = ["linux-pam-devel"]
pkgdesc = "Dinit user instance manager"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-2-Clause"
url = "https://github.com/chimera-linux/dinit-userservd"
source = f"https://github.com/chimera-linux/{pkgname}/archive/{_commit}.tar.gz"
sha256 = "256d68975be8e04305ee7ffea2b020aba94a48af77bbcbeba46288c52c974d55"

@subpackage("dinit-userservd-dbus")
def _dbus(self):
    self.pkgdesc = f"{pkgdesc} (dbus session runner)"
    self.depends = ["dbus"]
    self.install_if = [f"{pkgname}={pkgver}-r{pkgrel}", "dbus"]

    return ["usr/bin/dinit-run-dbus"]
