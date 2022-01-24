pkgname = "mobile-broadband-provider-info"
pkgver = "20210805"
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
sha256 = "3daf09b538a0ef0c47c65603c41862e9a6179853e495092c02bfce14c8fe287f"

def pre_configure(self):
    self.do("autoreconf", "-if")

def post_install(self):
    self.install_license("COPYING")
