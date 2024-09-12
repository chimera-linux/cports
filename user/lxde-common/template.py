pkgname = "lxde-common"
pkgver = "0.99.2"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["automake", "gettext-devel", "intltool", "pkgconf"]
makedepends = ["glib-devel"]
pkgdesc = "LXDE Session default configuration files"
maintainer = "jabuxas <jabuxas@proton.me>"
license = "GPL-2.0-only"
url = "https://github.com/lxde/lxde-common"
source = f"https://downloads.sourceforge.net/lxde/lxde-common-{pkgver}.tar.xz"
sha256 = "1cd9bc900960c995d48ffbbdc86ecffda7c806168c67aaa50c53113794234856"
# no tests
options = ["!check"]


@subpackage("lxde-backgrounds")
def _(self):
    self.pkgdesc = "Backgrounds for the LXDE desktop"
    self.install_if = [self.parent]

    return ["usr/share/lxde/wallpapers"]
