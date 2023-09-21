pkgname = "lisgd"
pkgver = "0.3.7"
pkgrel = 0
build_style = "makefile"
make_cmd = "gmake"
hostmakedepends = ["gmake"]
makedepends = ["libinput-devel", "libx11-devel", "wayland-devel"]
pkgdesc = "Bind gestures on touchscreens and other devices via libinput"
maintainer = "Froggo <froggo8311@proton.me>"
license = "MIT"
url = "https://git.sr.ht/~mil/lisgd"
source = f"{url}/archive/{pkgver}.tar.gz"
sha256 = "e4c5751984ef1f8d21f6f6548c184bca21a626b345fa0489e94f276ca49e950e"
# no check target
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
