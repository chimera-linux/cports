pkgname = "xfce4-dev-tools"
pkgver = "4.18.0"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--prefix=/usr",
    "--sysconfdir=/etc",
    "--libexecdir=/usr/lib",
    "--localstatedir=/var",
    "--disable-static",
]
hostmakedepends = ["automake", "libtool", "gtk-doc-tools", "pkgconf", "glib-devel"]
pkgdesc = "Xfce developer tools"
maintainer = "Sachin-Bhat <sachubhat17@gmail.com>"
license = "GPL-2.0-or-later"
url = "https://xfce.org"
source = f"https://archive.xfce.org/src/xfce/{pkgname}/{pkgver.rsplit('.', 1)[0]}/{pkgname}-{pkgver}.tar.bz2"
sha256 = "eedb4fc955f0e3459c46864ff98579295db2b900743e0ff69cad5970ba76be37"

def configure(self):
    self.run("./configure", *configure_args)

def build(self):
    self.run("make")

def install(self):
    self.run("make", f"DESTDIR={self.package_dir}", "install")
