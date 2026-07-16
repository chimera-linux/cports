pkgname = "kwallet-pam"
pkgver = "6.7.3"
pkgrel = 0
build_style = "cmake"
hostmakedepends = ["cmake", "extra-cmake-modules", "ninja", "pkgconf"]
makedepends = [
    "kwallet-devel",
    "libgcrypt-devel",
    "linux-pam-devel",
    "qt6-qtdeclarative-devel",
]
depends = ["socat"]
pkgdesc = "KDE KWallet PAM plugin"
license = "LGPL-2.1-or-later"
url = "https://invent.kde.org/plasma/kwallet-pam"
source = f"$(KDE_SITE)/plasma/{pkgver}/kwallet-pam-{pkgver}.tar.xz"
sha256 = "a720a1440edf8734e4b8d4d4d5ea96fc14946c21f38f6a5ca1b738d8a8dc583b"
hardening = ["vis"]
options = ["etcfiles"]


def post_install(self):
    # TODO: dinit user service with graphical
    self.uninstall("usr/lib/systemd/user")
