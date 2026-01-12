pkgname = "kio-admin"
pkgver = "25.12.1"
pkgrel = 0
build_style = "cmake"
# XXX drop libexec
configure_args = ["-DQT_MAJOR_VERSION=6", "-DCMAKE_INSTALL_LIBEXECDIR=/usr/lib"]
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
    "pkgconf",
]
makedepends = [
    "ki18n-devel",
    "kio-devel",
    "polkit-qt-1-devel",
    "qt6-qtbase-devel",
]
pkgdesc = "KDE KIO admin:// protocol implementation"
license = "GPL-2.0-only OR GPL-3.0-only"
url = "https://invent.kde.org/system/kio-admin"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/kio-admin-{pkgver}.tar.xz"
sha256 = "a96c0e2564205c40ae12733230410480ad9429daa64b3b0ae5cdbb8d1b958839"
hardening = ["vis"]
