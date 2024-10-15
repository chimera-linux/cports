pkgname = "plasma-workspace-wallpapers"
pkgver = "6.2.1"
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
sha256 = "5cc6d5fcd265eae0285b3a9b7cfa1aacb6219abe8f71656a2824cd3ee3e4f221"
