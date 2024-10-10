pkgname = "calendarsupport"
pkgver = "24.08.2"
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
    "akonadi-notes-devel",
    "kcalendarcore-devel",
    "kcalutils-devel",
    "kcalutils-devel",
    "kcodecs-devel",
    "kguiaddons-devel",
    "kholidays-devel",
    "ki18n-devel",
    "kidentitymanagement-devel",
    "kio-devel",
    "kmime-devel",
    "ktextaddons-devel",
    "qt6-qtdeclarative-devel",
]
checkdepends = ["xwayland-run"]
pkgdesc = "KDE library for calendar support"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "LGPL-2.0-or-later AND GPL-3.0-only"
url = "https://api.kde.org/kdepim/calendarsupport/html"
source = (
    f"$(KDE_SITE)/release-service/{pkgver}/src/calendarsupport-{pkgver}.tar.xz"
)
sha256 = "6eb4550dcc43f459db1f28237757e4957485df082281182b289eefc20d186bb5"


@subpackage("calendarsupport-devel")
def _(self):
    self.depends += [
        "akonadi-calendar-devel",
        "kidentitymanagement-devel",
        "kmime-devel",
        "qt6-qtbase-devel",
    ]
    return self.default_devel()
