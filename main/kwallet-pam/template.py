pkgname = "kwallet-pam"
pkgver = "6.7.1"
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
sha256 = "2f371edd8e4347d5b8af0e2a687f5e35377bfdd896c705c93b83ece0439e9c45"
hardening = ["vis"]


def post_install(self):
    # TODO: dinit user service with graphical
    self.uninstall("usr/lib/systemd/user")
