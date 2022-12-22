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
source = f"https://github.com/chimera-linux/turnstile/archive/refs/tags/{pkgname}-{pkgver}.tar.gz"
sha256 = "c3cfa87a5fe385ecd280dc57d18028158c924ee9f38276c82b06ce208b3b67a2"
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

# FIXME visibility
hardening = ["!vis"]
