pkgname = "kdialog"
pkgver = "24.05.0"
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
sha256 = "8b7d922affbb415af0cfd43de8612e1dad8eb3e5b8d3f43284f1bd50dee0b240"
# CFI: check
hardening = ["vis", "!cfi"]
# TODO
options = ["!cross"]
