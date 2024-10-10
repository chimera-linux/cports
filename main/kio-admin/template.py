pkgname = "kio-admin"
pkgver = "24.08.2"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DQT_MAJOR_VERSION=6"]
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
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "GPL-2.0-only OR GPL-3.0-only"
url = "https://invent.kde.org/system/kio-admin"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/kio-admin-{pkgver}.tar.xz"
sha256 = "f7e0529199a161a6b3d329f037b01486e959c5ee837b9deb85d0c7cf1f187263"
hardening = ["vis"]
