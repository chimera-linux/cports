pkgname = "xdg-utils"
pkgver = "1.1.3"
pkgrel = 1
_commit = "8ae02631a9806da11b34cd6b274af02d28aee5da"
build_style = "gnu_configure"
configure_gen = []
make_cmd = "gmake"
make_dir = "."
hostmakedepends = ["xmlto", "lynx", "gmake"]
pkgdesc = "Basic desktop integration scripts"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://www.freedesktop.org/wiki/Software/xdg-utils"
source = (
    f"https://gitlab.freedesktop.org/xdg/{pkgname}/-/archive/{_commit}.tar.gz"
)
sha256 = "c761bbb0c1f6d21a39e52690909ba57c9d120ec20919d3c4aa0353c834470ed6"
hardening = ["vis", "cfi"]
# no check target
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")


@subpackage("xdg-utils-x11")
def _x11(self):
    self.pkgdesc = f"{pkgdesc} (X11 integration)"
    self.build_style = "meta"
    self.depends = [f"{pkgname}={pkgver}-r{pkgrel}", "xset"]
    self.install_if = [f"{pkgname}={pkgver}-r{pkgrel}", "xserver-xorg-core"]

    return []
