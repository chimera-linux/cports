pkgname = "incidenceeditor"
pkgver = "26.08.0"
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
    "kholidays-devel",
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
license = "LGPL-2.0-or-later AND GPL-3.0-only"
url = "https://invent.kde.org/pim/incidenceeditor"
source = (
    f"$(KDE_SITE)/release-service/{pkgver}/src/incidenceeditor-{pkgver}.tar.xz"
)
sha256 = "79f17906af9f8328a40aab5cc4fea486a071dd867f642bd71a1ee4493b2e6ef1"


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
