pkgname = "xdg-utils"
pkgver = "1.2.1"
pkgrel = 0
build_style = "gnu_configure"
configure_gen = []
make_dir = "."
hostmakedepends = ["xmlto", "lynx"]
pkgdesc = "Basic desktop integration scripts"
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
def _(self):
    self.subdesc = "X11 integration"
    self.options = ["empty"]
    self.depends = [self.parent, "xset"]
    self.install_if = [self.parent, "xserver-xorg-core"]

    return []
