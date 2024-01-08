pkgname = "screen"
pkgver = "4.9.1"
pkgrel = 1
build_style = "gnu_configure"
configure_args = [
    "--enable-pam",
    "--enable-colors256",
    "--enable-rxvt_osc",
    "--enable-telnet",
    "--enable-use-locale",
    "--with-pty-group=5",
    "--with-socket-dir=/run/screens",
    "--with-sys-screenrc=/etc/screenrc",
]
configure_gen = ["./autogen.sh"]
make_cmd = "gmake"
hostmakedepends = [
    "automake",
    "gmake",
    "libtool",
]
makedepends = [
    "ncurses-devel",
    "linux-pam-devel",
    "linux-headers",
]
pkgdesc = "GNU screen"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "https://www.gnu.org/software/screen"
source = f"$(GNU_SITE)/screen/screen-{pkgver}.tar.gz"
sha256 = "26cef3e3c42571c0d484ad6faf110c5c15091fbf872b06fa7aa4766c7405ac69"
hardening = ["vis", "cfi"]

tool_flags = {"CFLAGS": ["-Wno-deprecated-non-prototype"]}


def post_install(self):
    # bundled configs
    self.install_file("etc/etcscreenrc", "etc", name="screenrc")
    self.install_file("etc/screenrc", "etc/skel", name=".screenrc")
    # our configs
    self.install_file(self.files_path / "screen", "etc/pam.d")
    self.install_file(self.files_path / "screen.conf", "usr/lib/tmpfiles.d")
    # drop suid root
    (self.destdir / f"usr/bin/screen-{pkgver}").chmod(0o755)
