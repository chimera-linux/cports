pkgname = "turnstile"
pkgver = "0.1.0"
pkgrel = 0
_commit = "8b39b75e2cfa6cdc50ea8335c4881d3815912cc2"
build_style = "meson"
configure_args = ["-Dmanage_rundir=true"]
hostmakedepends = ["meson", "pkgconf", "scdoc"]
makedepends = ["linux-pam-devel"]
depends = ["dinit-chimera"]
pkgdesc = "Chimera user service manager and session tracker"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-2-Clause"
url = "https://github.com/chimera-linux/turnstile"
source = f"https://github.com/chimera-linux/turnstile/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "30c4f137be65df28d41e7901489eae418a16b21ab48b3e8e0667e7c5d0b795af"
hardening = ["vis", "cfi"]
options = ["brokenlinks", "!splitdinit"]

def post_install(self):
    # just make sure it exists
    self.install_dir("usr/lib/dinit.d/user/boot.d", empty = True)
    # linger
    self.install_dir("var/lib/turnstiled/linger", empty = True)
    # also default systemwide link
    self.install_dir("usr/lib/dinit.d/boot.d")
    self.install_link(
        "../turnstiled", "usr/lib/dinit.d/boot.d/turnstiled"
    )
