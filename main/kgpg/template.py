pkgname = "kgpg"
pkgver = "25.12.1"
pkgrel = 0
build_style = "cmake"
# flaky
make_check_args = [
    "-E",
    "(kgpg-export|kgpg-import|kgpg-encrypt|kgpg-disable|kgpg-genkey)",
]
make_check_env = {"QT_QPA_PLATFORM": "offscreen"}
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
    "pkgconf",
]
makedepends = [
    "akonadi-contacts-devel",
    "gpgme-devel",
    "karchive-devel",
    "kcodecs-devel",
    "kcontacts-devel",
    "kcoreaddons-devel",
    "kcrash-devel",
    "kdbusaddons-devel",
    "kdoctools-devel",
    "ki18n-devel",
    "kio-devel",
    "kjobwidgets-devel",
    "knotifications-devel",
    "kservice-devel",
    "kstatusnotifieritem-devel",
    "ktextwidgets-devel",
    "kwidgetsaddons-devel",
    "kwindowsystem-devel",
    "kxmlgui-devel",
    "qt6-qtdeclarative-devel",
]
pkgdesc = "KDE GnuPG interface"
license = "GPL-2.0-or-later"
url = "https://apps.kde.org/kgpg"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/kgpg-{pkgver}.tar.xz"
sha256 = "b776ef9e5a10a15e195f346bb4111f261d3bfed38b6921eb34e9d77614862d66"
