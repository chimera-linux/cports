pkgname = "kglobalacceld"
pkgver = "6.1.2"
pkgrel = 0
build_style = "cmake"
# needs full init of kglobalaccel
make_check_args = ["-E", "shortcutstest"]
make_check_env = {"QT_QPA_PLATFORM": "offscreen"}
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "ninja",
]
makedepends = [
    "kconfig-devel",
    "kcoreaddons-devel",
    "kcrash-devel",
    "kdbusaddons-devel",
    "kglobalaccel-devel",
    "kio-devel",
    "kservice-devel",
    "kwindowsystem-devel",
    "qt6-qtdeclarative-devel",
]
pkgdesc = "KDE Daemon for global keyboard shortcut functionality"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "LGPL-2.0-or-later"
url = "https://invent.kde.org/plasma/kglobalacceld"
source = f"$(KDE_SITE)/plasma/{pkgver}/kglobalacceld-{pkgver}.tar.xz"
sha256 = "27b39e674a6b66ba05b34e181b8b39ed084853bd87a072f3333ce4c423a668dc"
# FIXME: cfi breaks at least 50+ kwin tests (together with kidletime)
hardening = ["vis", "!cfi"]


def post_install(self):
    self.uninstall("usr/lib/systemd/user")


@subpackage("kglobalacceld-devel")
def _devel(self):
    self.depends += [f"{pkgname}={pkgver}-r{pkgrel}"]

    return self.default_devel()
