pkgname = "kactivitymanagerd"
pkgver = "6.4.5"
pkgrel = 0
build_style = "cmake"
# XXX drop libexec
configure_args = ["-DCMAKE_INSTALL_LIBEXECDIR=/usr/lib"]
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
sha256 = "de52518b901beeb58a6327316fcda345b3552305556c85a1c4b1133f9ab7a424"
hardening = ["vis"]


def post_install(self):
    self.uninstall("usr/lib/systemd/user")
