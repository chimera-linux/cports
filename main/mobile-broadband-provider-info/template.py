pkgname = "mobile-broadband-provider-info"
pkgver = "20251101"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "pkgconf", "libxslt-progs"]
checkdepends = ["libxml2-progs"]
pkgdesc = "Database of mobile broadband service providers"
license = "custom:none"
url = "https://gitlab.gnome.org/GNOME/mobile-broadband-provider-info"
source = (
    f"{url}/-/archive/{pkgver}/mobile-broadband-provider-info-{pkgver}.tar.gz"
)
sha256 = "8e8c34edb2264b0e7d9a3af17d5a92c689d9275a6329078e84ccfc8637c51cba"


def post_install(self):
    self.install_license("COPYING")
