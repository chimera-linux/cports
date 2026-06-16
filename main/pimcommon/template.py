pkgname = "pimcommon"
pkgver = "26.04.2"
pkgrel = 0
build_style = "cmake"
make_check_env = {"QT_QPA_PLATFORM": "offscreen"}
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "libxslt-progs",
    "ninja",
    "pkgconf",
]
makedepends = [
    "akonadi-contacts-devel",
    "akonadi-devel",
    "akonadi-search-devel",
    "karchive-devel",
    "kcmutils-devel",
    "kcodecs-devel",
    "kconfig-devel",
    "kcontacts-devel",
    "kcoreaddons-devel",
    "ki18n-devel",
    "kimap-devel",
    "kio-devel",
    "kitemmodels-devel",
    "kjobwidgets-devel",
    "kldap-devel",
    "knewstuff-devel",
    "kservice-devel",
    "ktextaddons-devel",
    "ktextwidgets-devel",
    "kwidgetsaddons-devel",
    "kxmlgui-devel",
    "libkdepim-devel",
    "plasma-activities-devel",
    "purpose-devel",
    "qt6-qtdeclarative-devel",
    "qt6-qttools-devel",
]
pkgdesc = "KDE PIM common library"
license = "LGPL-2.0-or-later AND GPL-3.0-only"
url = "https://api.kde.org/kdepim/pimcommon/html"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/pimcommon-{pkgver}.tar.xz"
sha256 = "a3558fb4cf677b07f73ac3e5f0c74c179c898b455115a62e6f44cb064cfe2f62"


@subpackage("pimcommon-devel")
def _(self):
    self.depends += [
        "akonadi-contacts-devel",
        "akonadi-devel",
        "kconfig-devel",
        "kcontacts-devel",
        "kimap-devel",
        "ktextaddons-devel",
        "libkdepim-devel",
        "plasma-activities-devel",
        "qt6-qtbase-devel",
    ]
    return self.default_devel()
