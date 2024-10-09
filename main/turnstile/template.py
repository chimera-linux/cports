pkgname = "turnstile"
pkgver = "0.1.10"
pkgrel = 3
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
sha256 = "186adf1402f3c63eecdbed241145cb029b7b1268c701a87381522d5b64583f2d"
file_modes = {
    "+usr/lib/dinit.d/user/boot.d": ("root", "root", 0o755, True),
}
hardening = ["vis", "cfi"]
options = ["brokenlinks", "!splitdinit"]


def post_install(self):
    self.install_license("COPYING.md")
    self.install_tmpfiles(self.files_path / "tmpfiles.conf")
    # also default systemwide link
    self.install_dir("usr/lib/dinit.d/boot.d")
    self.install_link("usr/lib/dinit.d/boot.d/turnstiled", "../turnstiled")
