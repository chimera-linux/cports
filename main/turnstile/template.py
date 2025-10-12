pkgname = "turnstile"
pkgver = "0.1.11"
pkgrel = 0
build_style = "meson"
configure_args = [
    "--libexecdir=/usr/lib",  # XXX libexec
    "-Dmanage_rundir=true",
    "-Dpamdir=/usr/lib/pam.d",
]
hostmakedepends = ["meson", "pkgconf", "scdoc"]
makedepends = ["dinit-chimera", "linux-pam-devel"]
depends = ["dinit-chimera"]
provides = [
    self.with_pkgver("usvc:graphical.target"),
    self.with_pkgver("usvc:login.target"),
]
pkgdesc = "Chimera user service manager and session tracker"
license = "BSD-2-Clause"
url = "https://github.com/chimera-linux/turnstile"
source = f"https://github.com/chimera-linux/turnstile/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "04904eff68a726bed281820b3497e018ede55a5d745f31ceb9a502f905d0ed56"
file_modes = {
    "+usr/lib/dinit.d/user/boot.d": ("root", "root", 0o755, True),
}
hardening = ["vis", "cfi"]
options = ["brokenlinks", "!splitdinit"]


def post_install(self):
    self.install_license("COPYING.md")
    self.install_tmpfiles(self.files_path / "tmpfiles.conf")
    # also default systemwide link
    self.rename("etc/dinit.d", "usr/lib/dinit.d", relative=False)
    self.install_dir("usr/lib/dinit.d/boot.d")
    self.install_link("usr/lib/dinit.d/boot.d/turnstiled", "../turnstiled")
