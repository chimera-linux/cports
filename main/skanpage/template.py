pkgname = "skanpage"
pkgver = "26.08.3"
pkgrel = 0
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
]
makedepends = [
    "kconfig-devel",
    "kcoreaddons-devel",
    "kcrash-devel",
    "ki18n-devel",
    "kio-devel",
    "kirigami-devel",
    "kquickimageeditor-devel",
    "ksanecore-devel",
    "kxmlgui-devel",
    "leptonica-devel",
    "purpose-devel",
    "qt6-qtbase-devel",
    "qt6-qtdeclarative-devel",
    "qt6-qtwebengine-devel",  # Qt PDF
    "tesseract-devel",
]
pkgdesc = "Scanning utility for images and multi-page documents"
license = "GPL-2.0-only OR GPL-3.0-only"
url = "https://apps.kde.org/skanpage"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/skanpage-{pkgver}.tar.xz"
sha256 = "f2c753349f8d9e49114ed037615baab54948a528ca7f464f730b7099e19a8e6f"
