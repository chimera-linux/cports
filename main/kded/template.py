pkgname = "kded"
pkgver = "6.14.0"
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
license = "LGPL-2.1-only AND LGPL-2.1-or-later"
url = "https://api.kde.org/frameworks/kded/html"
source = (
    f"$(KDE_SITE)/frameworks/{pkgver[: pkgver.rfind('.')]}/kded-{pkgver}.tar.xz"
)
sha256 = "59f1aec94bd0176eba8bffd35a6ad5925b6d40702e26ee1697a46b3a4617d1ca"
hardening = ["vis"]


def post_install(self):
    self.uninstall("usr/lib/systemd/user")


@subpackage("kded-devel")
def _(self):
    self.depends += [self.parent]

    return self.default_devel()
