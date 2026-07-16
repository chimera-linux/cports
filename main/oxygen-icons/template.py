pkgname = "oxygen-icons"
pkgver = "6.28.0"
pkgrel = 0
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "ninja",
    "pkgconf",
]
makedepends = [
    "qt6-qtbase-devel",
]
checkdepends = [
    "fdupes",
]
pkgdesc = "Oxygen icon themes"
license = "GPL-2.0-or-later"
url = "https://api.kde.org/frameworks/oxygen-icons/html"
source = f"$(KDE_SITE)/frameworks/{pkgver[: pkgver.rfind('.')]}/oxygen-icons-{pkgver}.tar.xz"
sha256 = "d1dec052a8a02fcda4e584ba060ca4ac9e7b0433f259b4a2d32c5098d22fb614"
