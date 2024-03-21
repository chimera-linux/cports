pkgname = "pinentry"
# Keep pkgver in sync with contrib/pinentry-qt
pkgver = "1.3.0"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--enable-pinentry-tty",
    "--enable-pinentry-curses",
    "--enable-pinentry-gnome3",
    "--enable-fallback-curses",
    "--enable-libsecret",
    "--enable-ncurses",
]
configure_gen = ["./autogen.sh"]
hostmakedepends = ["automake", "gettext", "libtool", "pkgconf"]
makedepends = [
    "gcr-devel",
    "gettext-devel",
    "gtk+3-devel",
    "libassuan-devel",
    "libgpg-error-devel",
    "libsecret-devel",
    "ncurses-devel",
]
depends = ["cmd:pinentry!pinentry-curses-default"]
pkgdesc = "PIN or passphrase entry dialogs for GnuPG"
maintainer = "eater <=@eater.me>"
license = "GPL-2.0-or-later"
url = "https://www.gnupg.org/related_software/pinentry/index.html"
source = f"https://gnupg.org/ftp/gcrypt/{pkgname}/{pkgname}-{pkgver}.tar.bz2"
sha256 = "9b3cd5226e7597f2fded399a3bc659923351536559e9db0826981bca316494de"
options = ["empty"]


def post_install(self):
    # wipe the default symlink, user-chosen (curses is default)
    self.rm(self.destdir / "usr/bin/pinentry")


def _frontend(name):
    @subpackage(f"pinentry-{name}")
    def _name(self):
        self.pkgdesc = f"{pkgdesc} ({name} frontend)"
        return [f"usr/bin/pinentry-{name}"]

    @subpackage(f"pinentry-{name}-default")
    def _default(self):
        self.depends = [f"pinentry-{name}={pkgver}-r{pkgrel}"]
        if name == "curses":
            self.install_if = [f"pinentry-{name}={pkgver}-r{pkgrel}"]

        def inst():
            self.mkdir(self.destdir / "usr/bin", parents=True)
            self.ln_s(f"pinentry-{name}", self.destdir / "usr/bin/pinentry")

        return inst


for _fe in ["curses", "tty", "gnome3"]:
    _frontend(_fe)
