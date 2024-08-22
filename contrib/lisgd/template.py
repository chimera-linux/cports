pkgname = "lisgd"
pkgver = "0.4.0"
pkgrel = 0
build_style = "makefile"
makedepends = ["libinput-devel", "libx11-devel", "wayland-devel"]
pkgdesc = "Bind gestures on touchscreens and other devices via libinput"
maintainer = "Nova <froggo8311@proton.me>"
license = "MIT"
url = "https://git.sr.ht/~mil/lisgd"
source = f"{url}/archive/{pkgver}.tar.gz"
sha256 = "1eef0a3c4c297714b52dd061d40611c955ea8479ef3e60cfb0f7ab9cb22e65e7"
# no check target
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
