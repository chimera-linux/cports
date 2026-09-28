pkgname = "waycheck"
pkgver = "1.7.0"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "meson",
    "pkgconf",
]
makedepends = ["qt6-qtwayland-devel"]
checkdepends = ["appstream"]
pkgdesc = "GUI that displays the protocols implemented by a Wayland compositor"
license = "Apache-2.0"
url = "https://gitlab.freedesktop.org/serebit/waycheck"
source = f"{url}/-/archive/v{pkgver}.tar.gz"
sha256 = "135c375c8b6c35ddffc577b757b812dd96852fa039247d7adc0584168e870fe9"
