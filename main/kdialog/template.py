pkgname = "kdialog"
pkgver = "25.08.0"
pkgrel = 0
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
    "pkgconf",
]
makedepends = [
    "kdbusaddons-devel",
    "kguiaddons-devel",
    "kiconthemes-devel",
    "kio-devel",
    "knotifications-devel",
    "ktextwidgets-devel",
    "kwindowsystem-devel",
]
pkgdesc = "KDE dialog displayer"
license = "GPL-2.0-or-later"
url = "https://develop.kde.org/docs/administration/kdialog"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/kdialog-{pkgver}.tar.xz"
sha256 = "7772cdfe2acccfda420c627a8b1f4cf35acc1906f5155fc2166ee482e10755a3"
hardening = ["vis"]
# TODO
options = ["!cross"]
