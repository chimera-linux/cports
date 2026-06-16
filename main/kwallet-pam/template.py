pkgname = "kwallet-pam"
pkgver = "6.7.0"
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
sha256 = "71dbd5d6ab5243e78c523ce382d53bd14c35731af09497fbe929bca41b69aed9"
hardening = ["vis"]


def post_install(self):
    # TODO: dinit user service with graphical
    self.uninstall("usr/lib/systemd/user")
