pkgname = "plasma-workspace-wallpapers"
pkgver = "6.0.5"
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
sha256 = "7eab4d34735edffa1222b2b55fd2448d7f6235e45e00a1bf9a9450d736b53bf0"
