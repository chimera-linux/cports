pkgname = "akonadi-calendar"
pkgver = "24.12.0"
pkgrel = 0
build_style = "cmake"
# FIXME: ?
make_check_args = ["-E", "kcalcoreserializertest"]
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
    "kcalendarcore-devel",
    "kcalutils-devel",
    "kcodecs-devel",
    "kcrash-devel",
    "kdbusaddons-devel",
    "ki18n-devel",
    "kidentitymanagement-devel",
    "kio-devel",
    "kmailtransport-devel",
    "kmime-devel",
    "knotifications-devel",
    "kwidgetsaddons-devel",
    "kxmlgui-devel",
    "libkleo-devel",
    "messagelib-devel",
    "qt6-qtdeclarative-devel",
]
checkdepends = ["xwayland-run"]
pkgdesc = "KDE Akonadi calendar libraries"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "LGPL-2.1-or-later AND GPL-2.0-or-later"
url = "https://api.kde.org/kdepim/akonadi-calendar/html"
source = (
    f"$(KDE_SITE)/release-service/{pkgver}/src/akonadi-calendar-{pkgver}.tar.xz"
)
sha256 = "dfa4d60162bc3672ff3a76745f727e87b7a5e089be6b79f399b0df23970eba69"


@subpackage("akonadi-calendar-devel")
def _(self):
    self.depends += [
        "akonadi-devel",
        "kcalendarcore-devel",
        "ki18n-devel",
        "kidentitymanagement-devel",
        "kwidgetsaddons-devel",
    ]
    return self.default_devel()
