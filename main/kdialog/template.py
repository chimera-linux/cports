pkgname = "kdialog"
pkgver = "24.08.3"
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
maintainer = "psykose <alice@ayaya.dev>"
license = "GPL-2.0-or-later"
url = "https://develop.kde.org/docs/administration/kdialog"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/kdialog-{pkgver}.tar.xz"
sha256 = "781a2e9b456563f06d9a2c0d3feac54f156b6b8d0d18094aa2b7a1cb45796fc3"
hardening = ["vis"]
# TODO
options = ["!cross"]
