pkgname = "kwallet-pam"
pkgver = "6.4.0"
pkgrel = 0
build_style = "cmake"
# XXX drop libexec
configure_args = ["-DCMAKE_INSTALL_LIBEXECDIR=/usr/lib"]
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
sha256 = "450e4d6b804c597eb51159000e193688926e4d8225ae19a1627e25d11feb8b5e"
hardening = ["vis"]


def post_install(self):
    # TODO: dinit user service with graphical
    self.uninstall("usr/lib/systemd/user")
