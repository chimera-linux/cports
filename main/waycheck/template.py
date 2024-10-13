pkgname = "waycheck"
pkgver = "1.4.0"
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
sha256 = "0dd64dd2521bb41579cb7dcb249d9ccf90119ea6ece107ebb3ea452dd0a610c9"
