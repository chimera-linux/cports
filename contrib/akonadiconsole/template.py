pkgname = "akonadiconsole"
pkgver = "24.05.1"
pkgrel = 0
build_style = "cmake"
make_check_wrapper = ["wlheadless-run", "--"]
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
    "pkgconf",
]
makedepends = [
    "akonadi-contacts-devel",
    "akonadi-devel",
    "akonadi-mime-devel",
    "akonadi-search-devel",
    "calendarsupport-devel",
    "kcalendarcore-devel",
    "kcompletion-devel",
    "kcompletion-devel",
    "kconfig-devel",
    "kcontacts-devel",
    "kcrash-devel",
    "kdbusaddons-devel",
    "kdoctools-devel",
    "ki18n-devel",
    "kio-devel",
    "kitemmodels-devel",
    "kitemviews-devel",
    "kmime-devel",
    "ktextwidgets-devel",
    "kwidgetsaddons-devel",
    "kxmlgui-devel",
    "libkdepim-devel",
    "messagelib-devel",
    "qt6-qtdeclarative-devel",
    "xapian-core-devel",
]
checkdepends = ["xwayland-run"]
pkgdesc = "KDE Akonadi debug console"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "LGPL-2.1-or-later AND GPL-2.0-or-later"
url = "https://techbase.kde.org/KDE_PIM/Akonadi/Development_Tools"
source = (
    f"$(KDE_SITE)/release-service/{pkgver}/src/akonadiconsole-{pkgver}.tar.xz"
)
sha256 = "812a28a679be719847c04f01c1d26f3545c4548060a70c11f79cb7f8654b5aea"
