pkgname = "kactivitymanagerd"
pkgver = "6.7.5"
pkgrel = 0
build_style = "cmake"
hostmakedepends = ["cmake", "extra-cmake-modules", "gettext", "ninja"]
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
license = "GPL-2.0-only OR GPL-3.0-only"
url = "https://invent.kde.org/plasma/kactivitymanagerd"
source = f"$(KDE_SITE)/plasma/{pkgver}/kactivitymanagerd-{pkgver}.tar.xz"
sha256 = "6e549b0dacd28797153696e4ee27f8e19aee6f3711f94ee379b8fae8ecfd937a"
hardening = ["vis"]


def post_install(self):
    self.uninstall("usr/lib/systemd/user")
