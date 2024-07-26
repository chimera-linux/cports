pkgname = "turnstile"
pkgver = "0.1.9"
pkgrel = 0
build_style = "meson"
configure_args = ["-Dmanage_rundir=true", "-Dpamdir=/usr/lib/pam.d"]
hostmakedepends = ["meson", "pkgconf", "scdoc"]
makedepends = ["linux-pam-devel"]
depends = ["dinit-chimera"]
pkgdesc = "Chimera user service manager and session tracker"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-2-Clause"
url = "https://github.com/chimera-linux/turnstile"
source = f"https://github.com/chimera-linux/turnstile/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "1a23f8a6d4fdcfd195cee042cead0ff4d9e9e10ad97721435b86775a8a4e660d"
hardening = ["vis", "cfi"]
options = ["brokenlinks", "!splitdinit"]


def post_install(self):
    self.install_license("COPYING.md")
    # just make sure it exists
    self.install_dir("usr/lib/dinit.d/user/boot.d", empty=True)
    # linger
    self.install_dir("var/lib/turnstiled/linger", empty=True)
    # also default systemwide link
    self.install_dir("usr/lib/dinit.d/boot.d")
    self.install_link("usr/lib/dinit.d/boot.d/turnstiled", "../turnstiled")
