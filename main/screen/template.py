pkgname = "screen"
pkgver = "5.0.2"
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
license = "GPL-3.0-or-later"
url = "https://www.gnu.org/software/screen"
source = f"$(GNU_SITE)/screen/screen-{pkgver}.tar.gz"
sha256 = "ca9a2c7e240919bc7ac12124593ae4529bb4eb5f7349d8857829b7e3f0b3b332"
hardening = ["vis", "cfi"]
# don't build due to type errors
options = ["etcfiles", "!check"]


def post_install(self):
    # bundled configs
    self.install_file("etc/etcscreenrc", "etc", name="screenrc")
    self.install_file("etc/screenrc", "etc/skel", name=".screenrc")
    # our configs
    self.install_file(self.files_path / "screen", "usr/lib/pam.d")
    self.install_tmpfiles(self.files_path / "screen.conf")
    # drop suid root
    (self.destdir / f"usr/bin/screen-{pkgver}").chmod(0o755)
