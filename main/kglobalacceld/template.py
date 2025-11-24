pkgname = "kglobalacceld"
pkgver = "6.5.3"
pkgrel = 0
build_style = "cmake"
# XXX drop libexec
configure_args = ["-DCMAKE_INSTALL_LIBEXECDIR=/usr/lib"]
# needs full init of kglobalaccel
make_check_args = ["-E", "shortcutstest"]
make_check_env = {"QT_QPA_PLATFORM": "offscreen"}
hostmakedepends = ["cmake", "extra-cmake-modules", "ninja"]
makedepends = [
    "kconfig-devel",
    "kcoreaddons-devel",
    "kcrash-devel",
    "kdbusaddons-devel",
    "kglobalaccel-devel",
    "kio-devel",
    "kservice-devel",
    "kwindowsystem-devel",
    "qt6-qtbase-private-devel",  # qtx11extras_p.h
    "qt6-qtdeclarative-devel",
]
pkgdesc = "KDE Daemon for global keyboard shortcut functionality"
license = "LGPL-2.0-or-later"
url = "https://invent.kde.org/plasma/kglobalacceld"
source = f"$(KDE_SITE)/plasma/{pkgver}/kglobalacceld-{pkgver}.tar.xz"
sha256 = "47a9c9815b1dd34fd9ec77f2826ce959216f01275853375936434f12dc9287d2"
hardening = ["vis"]


def post_install(self):
    self.uninstall("usr/lib/systemd/user")


@subpackage("kglobalacceld-devel")
def _(self):
    self.depends += [self.parent]

    return self.default_devel()
