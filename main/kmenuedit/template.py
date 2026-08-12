pkgname = "kmenuedit"
pkgver = "6.7.4"
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
    "kcrash-devel",
    "kdbusaddons-devel",
    "kdoctools-devel",
    "kglobalaccel-devel",
    "ki18n-devel",
    "kiconthemes-devel",
    "kio-devel",
    "kitemviews-devel",
    "kwindowsystem-devel",
    "kxmlgui-devel",
    "qt6-qtdeclarative-devel",
    "sonnet-devel",
]
pkgdesc = "KDE menu editor"
license = "GPL-2.0-only"
url = "https://invent.kde.org/plasma/kmenuedit"
source = f"$(KDE_SITE)/plasma/{pkgver}/kmenuedit-{pkgver}.tar.xz"
sha256 = "bc8daed5c859904e580ca8415b88836fcde198957fa672b5b28de4017398b0c3"
hardening = ["vis"]
