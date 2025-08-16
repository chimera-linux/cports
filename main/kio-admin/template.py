pkgname = "kio-admin"
pkgver = "25.08.0"
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
sha256 = "21a57c0f7cb0c63f4e8497b5654be664655234b1b636880655040d33c2081613"
hardening = ["vis"]
