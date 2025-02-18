pkgname = "plasma-workspace-wallpapers"
pkgver = "6.3.1"
pkgrel = 0
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "ninja",
]
pkgdesc = "Wallpapers for Plasma Workspaces"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "LGPL-3.0-only AND CC-BY-SA-4.0"
url = "https://invent.kde.org/plasma/plasma-workspace-wallpapers"
source = (
    f"$(KDE_SITE)/plasma/{pkgver}/plasma-workspace-wallpapers-{pkgver}.tar.xz"
)
sha256 = "f4494bc3bbf16b67657f1fcf6bf62602bea6e9949a4e040744d557e7e177c60f"
