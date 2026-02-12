pkgname = "kde-inotify-survey"
pkgver = "25.12.2"
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
sha256 = "8383951e8d122275ec3d47a7a2a655ca0700f9ca92b8189b743b4e42e9a80ec7"
hardening = ["vis"]
# TODO
options = ["!cross"]
