pkgname = "kded"
pkgver = "6.7.0"
pkgrel = 0
build_style = "cmake"
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
    "kdoctools-devel",
    "kservice-devel",
    "qt6-qtdeclarative-devel",
]
pkgdesc = "Extensible central daemon of KDE workspaces"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "LGPL-2.1-only AND LGPL-2.1-or-later"
url = "https://api.kde.org/frameworks/kded/html"
source = (
    f"$(KDE_SITE)/frameworks/{pkgver[:pkgver.rfind('.')]}/kded-{pkgver}.tar.xz"
)
sha256 = "22aa1b6543b40e094346138516131c0f7eb78a70e87296938457fd1386680a2f"
hardening = ["vis"]


def post_install(self):
    self.uninstall("usr/lib/systemd/user")


@subpackage("kded-devel")
def _(self):
    self.depends += [self.parent]

    return self.default_devel()
