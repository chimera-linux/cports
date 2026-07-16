pkgname = "plasma-workspace-wallpapers"
pkgver = "6.7.3"
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
sha256 = "b8f5db6b254fdd75f9f28d0c6ff0af87dcbc3ec69c1a3881d5bdb70035071551"
