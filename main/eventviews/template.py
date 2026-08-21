pkgname = "eventviews"
pkgver = "26.08.0"
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
    "akonadi-calendar-devel",
    "akonadi-devel",
    "calendarsupport-devel",
    "kcalendarcore-devel",
    "kcalutils-devel",
    "kcodecs-devel",
    "kcompletion-devel",
    "kconfigwidgets-devel",
    "kcontacts-devel",
    "kdiagram-devel",
    "kguiaddons-devel",
    "kholidays-devel",
    "ki18n-devel",
    "kiconthemes-devel",
    "kitemmodels-devel",
    "kmime-devel",
    "kservice-devel",
    "libkdepim-devel",
    "qt6-qtdeclarative-devel",
]
checkdepends = ["xwayland-run"]
pkgdesc = "KDE event views library"
license = "LGPL-2.0-or-later AND GPL-2.0-or-later"
url = "https://community.kde.org/KDE_PIM"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/eventviews-{pkgver}.tar.xz"
sha256 = "aa4d8c8b968f804dc94c8ea3cccb379745b1b496b3fab7849113a5519b472477"


@subpackage("eventviews-devel")
def _(self):
    self.depends += [
        "akonadi-calendar-devel",
        "akonadi-devel",
        "calendarsupport-devel",
        "kcalendarcore-devel",
        "kcalutils-devel",
    ]
    return self.default_devel()
