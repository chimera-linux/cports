pkgname = "ydotool"
pkgver = "1.0.4"
pkgrel = 0
build_style = "cmake"
make_cmd = "make"
make_dir = "."
hostmakedepends = ["cmake", "pkgconf", "scdoc"]
makedepends = ["linux-headers"]
pkgdesc = "Generic command-line automation tool"
subdesc = "(like xdotool, but not for X11)"
license = "AGPL-3.0-or-later"
url = "https://github.com/ReimuNotMoe/ydotool"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "ba075a43aa6ead51940e892ecffa4d0b8b40c241e4e2bc4bd9bd26b61fde23bd"


def install(self):
    self.install_bin("ydotool")
    self.install_bin("ydotoold")


def post_install(self):
    self.install_man("manpage/ydotool.1")
    self.install_man("manpage/ydotoold.8")
    self.install_license("LICENSE")
