pkgname = "mobile-broadband-provider-info"
pkgver = "20230416"
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
sha256 = "36ceb37b0579cefb6da3113e6dc1059a00400bed2402ddbea9cc41f8fb031296"
# doesn't like our shell
options = ["!check"]

def pre_configure(self):
    self.do("autoreconf", "-if")

def post_install(self):
    self.install_license("COPYING")
