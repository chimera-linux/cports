pkgname = "screen"
pkgver = "5.0.0"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--enable-pam",
    "--enable-colors256",
    "--enable-rxvt_osc",
    "--enable-telnet",
    "--enable-use-locale",
    "--with-pty-group=5",
    "--enable-socket-dir=/run/screens",
    "--with-system_screenrc=/etc/screenrc",
]
configure_gen = ["./autogen.sh"]
make_dir = "."
hostmakedepends = ["automake"]
makedepends = [
    "linux-headers",
    "linux-pam-devel",
    "ncurses-devel",
]
pkgdesc = "GNU screen"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "https://www.gnu.org/software/screen"
source = f"$(GNU_SITE)/screen/screen-{pkgver}.tar.gz"
sha256 = "f04a39d00a0e5c7c86a55338808903082ad5df4d73df1a2fd3425976aed94971"
hardening = ["vis", "cfi"]
# don't build due to type errors
options = ["!check"]


def post_install(self):
    # bundled configs
    self.install_file("etc/etcscreenrc", "etc", name="screenrc")
    self.install_file("etc/screenrc", "etc/skel", name=".screenrc")
    # our configs
    self.install_file(self.files_path / "screen", "usr/lib/pam.d")
    self.install_tmpfiles(self.files_path / "screen.conf")
    # drop suid root
    (self.destdir / f"usr/bin/screen-{pkgver}").chmod(0o755)
