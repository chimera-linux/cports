pkgname = "rxvt-unicode"
pkgver = "9.30"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--with-terminfo=/usr/share/terminfo",
    "--with-term=rxvt-unicode-256color",
    "--enable-256-color",
    "--enable-font-styles",
    "--enable-keepscrolling",
    "--enable-selectionscrolling",
    "--enable-smart-resize",
    "--enable-transparency",
    "--enable-combining",
    "--enable-unicode3",
    "--enable-xim",
    "--disable-utmp",
    "--disable-wtmp",
    "--disable-lastlog",
    "--disable-frills",
    "--disable-perl",
    "--disable-pixbuf", # TODO: enable later
    "--disable-startup-notification", # TODO: enable later
]
hostmakedepends = ["pkgconf"]
makedepends = [
    "xorgproto", "libxrender-devel", "libxft-devel", "libxt-devel",
    "libsm-devel", "libptytty-devel", "fontconfig-devel",
]
depends = ["ncurses", f"rxvt-unicode-terminfo={pkgver}-r{pkgrel}"]
pkgdesc = "Terminal emulator supporting Xft fonts and Unicode"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "http://software.schmorp.de/pkg/rxvt-unicode.html"
source = f"http://dist.schmorp.de/{pkgname}/{pkgname}-{pkgver}.tar.bz2"
sha256 = "fe1c93d12f385876457a989fc3ae05c0915d2692efc59289d0f70fabe5b44d2d"

def init_configure(self):
    self.make_install_env["TERMINFO"] = \
        f"{self.chroot_destdir}/usr/share/terminfo"

def pre_install(self):
    self.make_install_env["TERMINFO"] = \
        f"{self.chroot_destdir}/usr/share/terminfo"

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
