pkgname = "eventviews"
pkgver = "24.12.0"
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
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "LGPL-2.0-or-later AND GPL-2.0-or-later"
url = "https://api.kde.org/kdepim/eventviews/html"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/eventviews-{pkgver}.tar.xz"
sha256 = "b8e9d473836cbb401fac0e1c41e01016b4853a6323530237113e3fece4403089"


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
