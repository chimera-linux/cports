pkgname = "pinentry"
pkgver = "1.2.1"
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
hostmakedepends = ["pkgconf", "automake", "libtool", "gettext"]
makedepends = [
    "ncurses-devel",
    "libassuan-devel",
    "libgpg-error-devel",
    "gcr-devel",
    "libsecret-devel",
    "gtk+3-devel",
    "gettext-devel",
]
depends = ["cmd:pinentry!pinentry-curses-default"]
pkgdesc = "PIN or passphrase entry di:alogs for GnuPG"
maintainer = "eater <=@eater.me>"
license = "GPL-2.0-or-later"
url = "https://www.gnupg.org/related_software/pinentry/index.html"
source = f"https://gnupg.org/ftp/gcrypt/{pkgname}/{pkgname}-{pkgver}.tar.bz2"
sha256 = "457a185e5a85238fb945a955dc6352ab962dc8b48720b62fc9fa48c7540a4067"
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
