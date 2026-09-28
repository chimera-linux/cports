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
hostmakedepends = ["automake", "pkgconf"]
makedepends = [
    "fontconfig-devel",
    "gdk-pixbuf-devel",
    "libptytty-devel",
    "libsm-devel",
    "libxft-devel",
    "libxrender-devel",
    "libxt-devel",
    "startup-notification-devel",
    "xorgproto",
]
depends = [self.with_pkgver("rxvt-unicode-terminfo")]
pkgdesc = "Terminal emulator supporting Xft fonts and Unicode"
license = "GPL-3.0-or-later"
url = "http://software.schmorp.de/pkg/rxvt-unicode.html"
source = f"http://dist.schmorp.de/rxvt-unicode/rxvt-unicode-{pkgver}.tar.bz2"
sha256 = "aaa13fcbc149fe0f3f391f933279580f74a96fd312d6ed06b8ff03c2d46672e8"
hardening = ["vis", "!cfi"]
# FIXME lintpixmaps
options = ["!lintpixmaps"]


def init_configure(self):
    self.make_install_env["TERMINFO"] = (
        f"{self.chroot_destdir}/usr/share/terminfo"
    )


def pre_install(self):
    self.make_install_env["TERMINFO"] = (
        f"{self.chroot_destdir}/usr/share/terminfo"
    )

    self.install_dir("usr/share/terminfo")


def post_install(self):
    self.install_file("doc/etc/rxvt-unicode.terminfo", "usr/share/terminfo/r")
    self.install_file(self.files_path / f"{pkgname}.png", "usr/share/pixmaps")
    self.install_file(
        self.files_path / f"{pkgname}.desktop", "usr/share/applications"
    )


@subpackage("rxvt-unicode-terminfo")
def _(self):
    self.subdesc = "terminfo data"

    return ["usr/share/terminfo"]
