pkgname = "kded"
pkgver = "6.22.0"
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
sha256 = "bfe540068c240dcf7451d6f573a452bb085ae536ee9d3fa2aee4065f9772f47d"
hardening = ["vis"]


def post_install(self):
    self.uninstall("usr/lib/systemd/user")


@subpackage("kded-devel")
def _(self):
    self.depends += [self.parent]

    return self.default_devel()
