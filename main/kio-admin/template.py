pkgname = "kio-admin"
pkgver = "25.08.1"
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
sha256 = "5f9fa99d0264906b5726f7bc5d710d1f606bdbb89fe79512f43dad1e8d64876f"
hardening = ["vis"]
