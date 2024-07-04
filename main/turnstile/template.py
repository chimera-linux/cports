pkgname = "turnstile"
pkgver = "0.1.8"
pkgrel = 4
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
sha256 = "7eaab8c80c76ae9a9a711d7dc57ec346b9af09be99b526a5a3129a7fc9bd7a76"
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
    # move pam.d stuff, FIXME in turnstile later
    self.mv("etc/pam.d", "usr/lib/pam.d", relative=False)
