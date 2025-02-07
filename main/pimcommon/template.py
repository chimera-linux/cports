pkgname = "pimcommon"
pkgver = "24.12.2"
pkgrel = 0
build_style = "cmake"
make_check_env = {"QT_QPA_PLATFORM": "offscreen"}
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
    "pkgconf",
    "libxslt-progs",
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
    "purpose-devel",
    "qt6-qtdeclarative-devel",
    "qt6-qttools-devel",
]
pkgdesc = "KDE PIM common library"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "LGPL-2.0-or-later AND GPL-3.0-only"
url = "https://api.kde.org/kdepim/pimcommon/html"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/pimcommon-{pkgver}.tar.xz"
sha256 = "6948e9930b5706944347fdeec69cd2bfd53331312919782aec111fea57d9650c"


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
        "qt6-qtbase-devel",
    ]
    return self.default_devel()
