pkgname = "kded"
pkgver = "6.9.0"
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
    f"$(KDE_SITE)/frameworks/{pkgver[: pkgver.rfind('.')]}/kded-{pkgver}.tar.xz"
)
sha256 = "39d74343db901b8419244738ef4c6d9e8b1a3331278d55f57811b016adb02a9f"
hardening = ["vis"]


def post_install(self):
    self.uninstall("usr/lib/systemd/user")


@subpackage("kded-devel")
def _(self):
    self.depends += [self.parent]

    return self.default_devel()
