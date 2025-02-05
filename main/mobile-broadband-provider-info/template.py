pkgname = "mobile-broadband-provider-info"
pkgver = "20240407"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "pkgconf", "libxslt-progs"]
checkdepends = ["libxml2-progs"]
pkgdesc = "Database of mobile broadband service providers"
maintainer = "q66 <q66@chimera-linux.org>"
license = "custom:none"
url = "https://gitlab.gnome.org/GNOME/mobile-broadband-provider-info"
source = (
    f"{url}/-/archive/{pkgver}/mobile-broadband-provider-info-{pkgver}.tar.gz"
)
sha256 = "0a3985bd38d23d8225a85c96a6b8e4afec022ece7bf0cc7efc43f296012f9699"


def post_install(self):
    self.install_license("COPYING")
