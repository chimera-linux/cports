pkgname = "ansifilter"
pkgver = "2.22"
pkgrel = 0
build_style = "cmake"
hostmakedepends = ["cmake", "ninja"]
makedepends = ["boost-devel", "qt6-qtbase-devel"]
pkgdesc = "ANSI escape codes parser"
license = "GPL-3.0-only"
url = "https://gitlab.com/saalen/ansifilter"
source = f"{url}/-/archive/{pkgver}/ansifilter-{pkgver}.tar.gz"
sha256 = "cf5b95564d95d398e78071f147ee3cbf850e6dc8226a86ecff2de4356f19ff66"
hardening = ["vis", "cfi"]


@subpackage("ansifilter-gui")
def _(self):
    self.depends = [self.parent]
    self.subdesc = "GUI"
    return [
        "cmd:ansifilter-gui",
        "usr/share/applications",
        "usr/share/icons",
    ]
