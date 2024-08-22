pkgname = "pinentry-qt"
# Keep pkgver in sync with main/pinentry
pkgver = "1.3.1"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--enable-pinentry-qt",
    "--enable-libsecret",
    "--disable-ncurses",
]
hostmakedepends = ["automake", "gettext", "libtool", "pkgconf"]
makedepends = [
    "gettext-devel",
    "kwindowsystem-devel",
    "libassuan-devel",
    "libgpg-error-devel",
    "libsecret-devel",
    "qt6-qtbase-devel",
]
origin = "pinentry"
pkgdesc = "Qt6 frontend for pinentry"
maintainer = "triallax <triallax@tutanota.com>"
license = "GPL-2.0-or-later"
url = "https://www.gnupg.org/related_software/pinentry/index.html"
source = f"https://gnupg.org/ftp/gcrypt/pinentry/pinentry-{pkgver}.tar.bz2"
sha256 = "bc72ee27c7239007ab1896c3c2fae53b076e2c9bd2483dc2769a16902bce8c04"


def post_install(self):
    # wipe the default symlink, user-chosen
    self.uninstall("usr/bin/pinentry")


@subpackage("pinentry-qt-default")
def _(self):
    self.depends = [self.parent]
    self.provides = ["pinentry-default=0"]

    return ["@usr/bin/pinentry=>pinentry-qt"]
