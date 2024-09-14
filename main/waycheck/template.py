pkgname = "waycheck"
pkgver = "1.3.1"
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
sha256 = "b8dce84a1bc9c54e08148c81e715398a0699bf186eb2592c83216bb87d0d973d"
