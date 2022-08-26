pkgname = "mobile-broadband-provider-info"
pkgver = "20220725"
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
sha256 = "801a1862b9908177275418c1fd6313d6c9e7c4b55ec99ea0552577d5316f1a38"
# doesn't like our shell
options = ["!check"]

def pre_configure(self):
    self.do("autoreconf", "-if")

def post_install(self):
    self.install_license("COPYING")
