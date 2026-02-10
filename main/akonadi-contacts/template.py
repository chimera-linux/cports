pkgname = "akonadi-contacts"
pkgver = "25.12.2"
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
    "akonadi-devel",
    "grantleetheme-devel",
    "kcodecs-devel",
    "kcompletion-devel",
    "kconfig-devel",
    "kcontacts-devel",
    "kcoreaddons-devel",
    "kguiaddons-devel",
    "ki18n-devel",
    "kiconthemes-devel",
    "kio-devel",
    "kmime-devel",
    "kservice-devel",
    "ktextaddons-devel",
    "ktexttemplate-devel",
    "ktextwidgets-devel",
    "kxmlgui-devel",
    "prison-devel",
    "qt6-qtdeclarative-devel",
]
checkdepends = ["xwayland-run"]
pkgdesc = "KDE Akonadi contacts libraries"
license = "LGPL-2.0-or-later AND GPL-2.0-or-later"
url = "https://api.kde.org/kdepim/akonadi-contacts/html/index.html"
source = (
    f"$(KDE_SITE)/release-service/{pkgver}/src/akonadi-contacts-{pkgver}.tar.xz"
)
sha256 = "fa4d6b95143478f7d44897c68c33ee0f030426f25d8567045b904c2a02eb3686"


@subpackage("akonadi-contacts-devel")
def _(self):
    self.depends += [
        "akonadi-devel",
        "grantleetheme-devel",
        "kcontacts-devel",
        "qt6-qtbase-devel",
    ]
    return self.default_devel()
