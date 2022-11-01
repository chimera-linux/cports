pkgname = "dinit-userservd"
pkgver = "0.91.0"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "pkgconf"]
makedepends = ["linux-pam-devel"]
pkgdesc = "Dinit user instance manager"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-2-Clause"
url = "https://github.com/chimera-linux/dinit-userservd"
source = f"https://github.com/chimera-linux/{pkgname}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "350d4a83fd77ce870a813bbf49bbbd69aa358b16d293bada8c53ec8dc1f6b6f6"
options = ["brokenlinks", "!splitdinit"]

def post_install(self):
    # just make sure it exists
    self.install_dir("usr/lib/dinit.d/user/boot.d", empty = True)
    # also default systemwide link
    self.install_dir("usr/lib/dinit.d/boot.d")
    self.install_link(
        "../dinit-userservd", "usr/lib/dinit.d/boot.d/dinit-userservd"
    )
