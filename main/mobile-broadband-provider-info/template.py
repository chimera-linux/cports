pkgname = "mobile-broadband-provider-info"
pkgver = "20220315"
pkgrel = 0
build_style = "gnu_configure"
make_cmd = "gmake"
hostmakedepends = ["gmake", "automake", "xsltproc", "pkgconf"]
checkdepends = ["libxml2-progs"]
pkgdesc = "Database of mobile broadband service providers"
maintainer = "q66 <q66@chimera-linux.org>"
license = "custom:none"
url = "https://gitlab.gnome.org/GNOME/mobile-broadband-provider-info"
source = f"{url}/-/archive/{pkgver}/{pkgname}-{pkgver}.tar.gz"
sha256 = "0776c8396f46487c31569d0e68a0d839f42ef1882db5bb0461a59880812ba9cf"

def pre_configure(self):
    self.do("autoreconf", "-if")

def post_install(self):
    self.install_license("COPYING")
