pkgname = "grantlee-editor"
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
sha256 = "b1951c2b786a2de909027f37c644474cbd8b4c0c93518aa25799c02d8f15bb07"
