pkgname = "calendarsupport"
pkgver = "25.08.2"
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
license = "LGPL-2.0-or-later AND GPL-3.0-only"
url = "https://api.kde.org/kdepim/calendarsupport/html"
source = (
    f"$(KDE_SITE)/release-service/{pkgver}/src/calendarsupport-{pkgver}.tar.xz"
)
sha256 = "2f3c3da6ff600c571c962e18cab7d2a6c780d79e282b94dec6d70a6f084d6d46"


@subpackage("calendarsupport-devel")
def _(self):
    self.depends += [
        "akonadi-calendar-devel",
        "kidentitymanagement-devel",
        "kmime-devel",
        "qt6-qtbase-devel",
    ]
    return self.default_devel()
