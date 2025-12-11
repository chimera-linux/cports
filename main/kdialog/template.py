pkgname = "kdialog"
pkgver = "25.12.0"
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
sha256 = "ef064b3e7ba83e1ac186147b430c442c47213801e6f66c0d3e3617468a0074a1"
hardening = ["vis"]
# TODO
options = ["!cross"]
