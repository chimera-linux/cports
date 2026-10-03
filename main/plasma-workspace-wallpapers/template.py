pkgname = "plasma-workspace-wallpapers"
pkgver = "6.7.91"
pkgrel = 0
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "ninja",
    "qt6-qtbase-devel",
]
pkgdesc = "Wallpapers for Plasma Workspaces"
license = "LGPL-3.0-only AND CC-BY-SA-4.0"
url = "https://invent.kde.org/plasma/plasma-workspace-wallpapers"
source = f"$(KDE_UNSTABLE_SITE)/plasma/{pkgver}/plasma-workspace-wallpapers-{pkgver}.tar.xz"
sha256 = "199209d64a1ba8f6c8530fb0abe0f90e9df4203646318e2fee4fabfb10874b9f"
