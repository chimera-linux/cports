pkgname = "pimcommon"
pkgver = "25.08.2"
pkgrel = 1
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
sha256 = "de341499406f317dafe9fa3e5eeb600bbd0ec69f34e28e8e0bb8ffdabe8e950b"


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
