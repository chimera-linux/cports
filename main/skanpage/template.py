pkgname = "skanpage"
pkgver = "26.08.1"
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
sha256 = "849338282311c9a2c936f3aae8f38be8b7ee7a890592912452eb4424e5a82b01"
