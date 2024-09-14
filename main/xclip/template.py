pkgname = "xclip"
pkgver = "0.13"
pkgrel = 0
build_style = "gnu_configure"
make_dir = "."
hostmakedepends = ["automake"]
makedepends = ["libxmu-devel"]
checkdepends = ["psmisc", "xwayland-run"]
pkgdesc = "Command line interface to the X11 clipboard"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "GPL-2.0-or-later"
url = "https://github.com/astrand/xclip"
source = f"{url}/archive/{pkgver}.tar.gz"
sha256 = "ca5b8804e3c910a66423a882d79bf3c9450b875ac8528791fb60ec9de667f758"
hardening = ["vis", "cfi"]


def check(self):
    self.do("xwfb-run", "--", "./xctest")
