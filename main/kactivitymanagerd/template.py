pkgname = "kactivitymanagerd"
pkgver = "6.3.1"
pkgrel = 0
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
]
makedepends = [
    "boost-devel",
    "kcrash-devel",
    "kdbusaddons-devel",
    "kglobalaccel-devel",
    "ki18n-devel",
    "kio-devel",
    "kxmlgui-devel",
    "qt6-qtdeclarative-devel",
]
# depends = ["qt6-qtbase-sql"]
pkgdesc = "KDE Manage user's activities and track usage patterns"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "GPL-2.0-only OR GPL-3.0-only"
url = "https://invent.kde.org/plasma/kactivitymanagerd"
source = f"$(KDE_SITE)/plasma/{pkgver}/kactivitymanagerd-{pkgver}.tar.xz"
sha256 = "b435fb044f66648b7c976979cbb8de1567fce3a511e84d61276d1637119cdea4"
hardening = ["vis"]


def post_install(self):
    self.uninstall("usr/lib/systemd/user")
