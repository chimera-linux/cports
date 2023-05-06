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
hostmakedepends = ["automake", "libtool", "gtk-doc-tools", "intltool", "pkgconf", "glib-devel"]  # intltool seems to not be packaged yet
makedepends = ["libglib-devel"]
depends = f"{hostmakedepends}"
pkgdesc = "Xfce developer tools"
maintainer = "Sachin-Bhat <sachubhat17@gmail.com>"
license = "GPL-2.0-or-later"
url = "https://xfce.org/"
source = f"https://archive.xfce.org/src/xfce/{pkgname}/{pkgver.rsplit('.', 1)[0]}/{pkgname}-{pkgver}.tar.bz2"
sha512 = "59f858b633d95585a74c9b9515a0994744f4355ab3813e582e10c776454ac41c86296a9fbd935d5dae88929ec09ec9c30f48629c7addb5729e6bea108d304f7c"

def configure(self):
    self.run("./configure", *configure_args)

def build(self):
    self.run("make")

def install(self):
    self.run("make", f"DESTDIR={self.package_dir}", "install")

@subpackage("xfce4-dev-tools-docs")
def _docs(self):
    return self.default_docs()
