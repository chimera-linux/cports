pkgname = "mobile-broadband-provider-info"
pkgver = "20221107"
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
sha256 = "09adf18f60300c6e402102c40d0c51d5b777e8e733b9d395abb2508a42f2dee9"
# doesn't like our shell
options = ["!check"]

def pre_configure(self):
    self.do("autoreconf", "-if")

def post_install(self):
    self.install_license("COPYING")
