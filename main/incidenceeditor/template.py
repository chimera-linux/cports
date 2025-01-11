pkgname = "incidenceeditor"
pkgver = "24.12.1"
pkgrel = 0
build_style = "cmake"
make_check_args = ["-E", "akonadi-sqlite-.*"]
make_check_wrapper = ["wlheadless-run", "--"]
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
    "pkgconf",
]
makedepends = [
    "akonadi-calendar-devel",
    "akonadi-devel",
    "akonadi-mime-devel",
    "calendarsupport-devel",
    "eventviews-devel",
    "kcalendarcore-devel",
    "kcalutils-devel",
    "kcodecs-devel",
    "kdiagram-devel",
    "kguiaddons-devel",
    "ki18n-devel",
    "kiconthemes-devel",
    "kidentitymanagement-devel",
    "kio-devel",
    "kldap-devel",
    "kmime-devel",
    "kpimtextedit-devel",
    "ktextwidgets-devel",
    "libkdepim-devel",
    "pimcommon-devel",
    "qt6-qtbase-devel",
]
checkdepends = ["xwayland-run"]
pkgdesc = "KDE PIM library for incidence editing"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "LGPL-2.0-or-later AND GPL-3.0-only"
url = "https://invent.kde.org/pim/incidenceeditor"
source = (
    f"$(KDE_SITE)/release-service/{pkgver}/src/incidenceeditor-{pkgver}.tar.xz"
)
sha256 = "89c3022b6b7afc4b79994d40f780409da5007743bfec91f495500bdd4071768e"


@subpackage("incidenceeditor-devel")
def _(self):
    self.depends += [
        "akonadi-mime-devel",
        "calendarsupport-devel",
        "eventviews-devel",
        "kcalendarcore-devel",
        "kcalutils-devel",
        "kmime-devel",
    ]
    return self.default_devel()
