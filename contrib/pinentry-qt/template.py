pkgname = "pinentry-qt"
# Keep pkgver in sync with main/pinentry
pkgver = "1.3.0"
pkgrel = 1
build_style = "gnu_configure"
configure_args = [
    "--enable-pinentry-qt",
    "--enable-libsecret",
    "--disable-ncurses",
]
configure_gen = ["./autogen.sh"]
make_cmd = "gmake"
hostmakedepends = ["automake", "gettext", "gmake", "libtool", "pkgconf"]
makedepends = [
    "gettext-devel",
    "libassuan-devel",
    "libgpg-error-devel",
    "libsecret-devel",
    "qt6-qtbase-devel",
]
origin = "pinentry"
pkgdesc = "PIN or passphrase entry dialogs for GnuPG (qt6 frontend)"
maintainer = "triallax <triallax@tutanota.com>"
license = "GPL-2.0-or-later"
url = "https://www.gnupg.org/related_software/pinentry/index.html"
source = f"https://gnupg.org/ftp/gcrypt/pinentry/pinentry-{pkgver}.tar.bz2"
sha256 = "9b3cd5226e7597f2fded399a3bc659923351536559e9db0826981bca316494de"


def post_install(self):
    # wipe the default symlink, user-chosen
    self.rm(self.destdir / "usr/bin/pinentry")


@subpackage("pinentry-qt-default")
def _default(self):
    self.depends = [f"pinentry-qt={pkgver}-r{pkgrel}"]
    self.provides = ["pinentry-default=0"]

    def inst():
        self.mkdir(self.destdir / "usr/bin", parents=True)
        self.ln_s("pinentry-qt", self.destdir / "usr/bin/pinentry")

    return inst
