pkgname = "kdialog"
pkgver = "26.08.3"
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
sha256 = "64cbdf30d29f26c0535d66494a3032860e700922deb44b3839e2ab171e639a66"
hardening = ["vis"]
# TODO
options = ["!cross"]
