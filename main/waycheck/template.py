pkgname = "waycheck"
pkgver = "1.5.0"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "meson",
    "pkgconf",
]
makedepends = ["qt6-qtwayland-devel"]
checkdepends = ["appstream"]
pkgdesc = "GUI that displays the protocols implemented by a Wayland compositor"
maintainer = "cassiofb-dev <contact@cassiofernando.com>"
license = "Apache-2.0"
url = "https://gitlab.freedesktop.org/serebit/waycheck"
source = f"{url}/-/archive/v{pkgver}.tar.gz"
sha256 = "74a4483c649de998959ada194d927e9de1e06e2d01af878413e4b389b5fbf45e"
