pkgname = "grantlee-editor"
pkgver = "25.12.2"
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
    "akonadi-contacts-devel",
    "grantleetheme-devel",
    "karchive-devel",
    "kcrash-devel",
    "kdbusaddons-devel",
    "kdoctools-devel",
    "kimap-devel",
    "kio-devel",
    "kmime-devel",
    "ktextaddons-devel",
    "kxmlgui-devel",
    "messagelib-devel",
    "pimcommon-devel",
    "qt6-qtbase-devel",
    "qt6-qtwebengine-devel",
    "syntax-highlighting-devel",
]
pkgdesc = "KDE editor for Grantlee themes"
license = "GPL-2.0-or-later"
url = "https://invent.kde.org/pim/grantlee-editor"
source = (
    f"$(KDE_SITE)/release-service/{pkgver}/src/grantlee-editor-{pkgver}.tar.xz"
)
sha256 = "e882087645db98bad54abd2c8f8be075bee878b25051884f1186f2c8b20f626a"
