pkgname = "plasma-workspace-wallpapers"
pkgver = "6.7.5"
pkgrel = 0
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "ninja",
]
pkgdesc = "Wallpapers for Plasma Workspaces"
license = "LGPL-3.0-only AND CC-BY-SA-4.0"
url = "https://invent.kde.org/plasma/plasma-workspace-wallpapers"
source = (
    f"$(KDE_SITE)/plasma/{pkgver}/plasma-workspace-wallpapers-{pkgver}.tar.xz"
)
sha256 = "c481ac4b937a2b1b080c3273e0557cd0c9d57b644156b941902483fd8e1646b5"
