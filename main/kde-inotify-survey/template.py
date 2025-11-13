pkgname = "kde-inotify-survey"
pkgver = "25.08.3"
pkgrel = 0
build_style = "cmake"
# XXX drop libexec
configure_args = ["-DCMAKE_INSTALL_LIBEXECDIR=/usr/lib"]
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
    "pkgconf",
]
makedepends = [
    "kauth-devel",
    "kcoreaddons-devel",
    "kdbusaddons-devel",
    "ki18n-devel",
    "knotifications-devel",
    "qt6-qtdeclarative-devel",
]
depends = ["kirigami-addons"]
checkdepends = ["xwayland-run", *depends]
pkgdesc = "KDE inotify limit monitor"
license = "GPL-2.0-only OR GPL-3.0-only"
url = "https://invent.kde.org/system/kde-inotify-survey"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/kde-inotify-survey-{pkgver}.tar.xz"
sha256 = "b39c129b96b80904f4a7b5f828ecd98891c32b61b9496e8d6310589da91eb95b"
hardening = ["vis"]
# TODO
options = ["!cross"]
