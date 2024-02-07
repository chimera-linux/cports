pkgname = "xdg-utils"
pkgver = "1.2.1"
pkgrel = 0
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
    f"https://gitlab.freedesktop.org/xdg/xdg-utils/-/archive/v{pkgver}.tar.gz"
)
sha256 = "61315926667f979921d3fda4471bed22aaeefcf84996e854786528bbcbcfbd8d"
hardening = ["vis", "cfi"]
# no check target
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")


@subpackage("xdg-utils-x11")
def _x11(self):
    self.pkgdesc = f"{pkgdesc} (X11 integration)"
    self.options = ["empty"]
    self.depends = [f"{pkgname}={pkgver}-r{pkgrel}", "xset"]
    self.install_if = [f"{pkgname}={pkgver}-r{pkgrel}", "xserver-xorg-core"]

    return []
