pkgname = "waycheck"
pkgver = "1.6.0"
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
sha256 = "ce19b05ef7739c0dc5b11d227c80b18ed1fb70c86822122ca50015b03e406bf5"
