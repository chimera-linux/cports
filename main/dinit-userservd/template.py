pkgname = "dinit-userservd"
pkgver = "0.92.0"
pkgrel = 0
build_style = "meson"
configure_args = ["-Dmanage_rundir=true"]
hostmakedepends = ["meson", "pkgconf", "scdoc"]
makedepends = ["linux-pam-devel"]
pkgdesc = "Dinit user instance manager"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-2-Clause"
url = "https://github.com/chimera-linux/dinit-userservd"
source = f"https://github.com/chimera-linux/{pkgname}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "af77af35c5d91c4cbfbabdb2dd015ec78a5b9c355501e3aea124e4b14efcd6c2"
options = ["brokenlinks", "!splitdinit"]

def post_install(self):
    # just make sure it exists
    self.install_dir("usr/lib/dinit.d/user/boot.d", empty = True)
    # linger
    self.install_dir("var/lib/dinit-userservd/linger", empty = True)
    # also default systemwide link
    self.install_dir("usr/lib/dinit.d/boot.d")
    self.install_link(
        "../dinit-userservd", "usr/lib/dinit.d/boot.d/dinit-userservd"
    )
