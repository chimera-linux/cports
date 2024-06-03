pkgname = "kwallet-pam"
pkgver = "6.0.5"
pkgrel = 0
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "ninja",
]
makedepends = [
    "kwallet-devel",
    "libgcrypt-devel",
    "linux-pam-devel",
    "qt6-qtdeclarative-devel",
]
depends = ["socat"]
pkgdesc = "KDE KWallet PAM plugin"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "LGPL-2.1-or-later"
url = "https://invent.kde.org/plasma/kwallet-pam"
source = f"$(KDE_SITE)/plasma/{pkgver}/kwallet-pam-{pkgver}.tar.xz"
sha256 = "25c61128eaefb563e500547f650be293e75126ed5fc2fac574ef40cccbfd00db"
# CFI: check
hardening = ["vis", "!cfi"]


def post_install(self):
    # TODO: dinit user service with graphical
    self.rm(self.destdir / "usr/lib/systemd/user", recursive=True)
