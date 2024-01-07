pkgname = "rxvt-unicode"
pkgver = "9.31"
pkgrel = 1
build_style = "gnu_configure"
configure_args = [
    "--with-terminfo=/usr/share/terminfo",
    "--with-term=rxvt-unicode-256color",
    "--enable-256-color",
    "--enable-font-styles",
    "--enable-keepscrolling",
    "--enable-startup-notification",
    "--enable-selectionscrolling",
    "--enable-smart-resize",
    "--enable-transparency",
    "--enable-combining",
    "--enable-unicode3",
    "--enable-pixbuf",
    "--enable-frills",
    "--enable-xim",
    "--disable-perl",
]
hostmakedepends = ["pkgconf"]
makedepends = [
    "xorgproto",
    "libxrender-devel",
    "libxft-devel",
    "libxt-devel",
    "libsm-devel",
    "libptytty-devel",
    "fontconfig-devel",
    "gdk-pixbuf-devel",
    "startup-notification-devel",
]
depends = [f"rxvt-unicode-terminfo={pkgver}-r{pkgrel}"]
pkgdesc = "Terminal emulator supporting Xft fonts and Unicode"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "http://software.schmorp.de/pkg/rxvt-unicode.html"
source = f"http://dist.schmorp.de/{pkgname}/{pkgname}-{pkgver}.tar.bz2"
sha256 = "aaa13fcbc149fe0f3f391f933279580f74a96fd312d6ed06b8ff03c2d46672e8"
hardening = ["vis", "!cfi"]


def init_configure(self):
    self.make_install_env[
        "TERMINFO"
    ] = f"{self.chroot_destdir}/usr/share/terminfo"


def pre_install(self):
    self.make_install_env[
        "TERMINFO"
    ] = f"{self.chroot_destdir}/usr/share/terminfo"

    self.install_dir("usr/share/terminfo")


def post_install(self):
    self.install_file("doc/etc/rxvt-unicode.terminfo", "usr/share/terminfo/r")
    self.install_file(self.files_path / f"{pkgname}.png", "usr/share/pixmaps")
    self.install_file(
        self.files_path / f"{pkgname}.desktop", "usr/share/applications"
    )


@subpackage("rxvt-unicode-terminfo")
def _tinfo(self):
    self.pkgdesc = f"{pkgdesc} (terminfo data)"

    return ["usr/share/terminfo"]


configure_gen = []
