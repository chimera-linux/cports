pkgname = "mobile-broadband-provider-info"
pkgver = "20250613"
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
sha256 = "b5168b7c886c6eac8bd844bb9aaaf12f3032444138d1d190e27772b5e55111ed"


def post_install(self):
    self.install_license("COPYING")
