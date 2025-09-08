pkgname = "ansifilter"
pkgver = "2.21"
pkgrel = 3
build_style = "cmake"
hostmakedepends = ["cmake", "ninja"]
makedepends = ["boost-devel", "qt6-qtbase-devel"]
pkgdesc = "ANSI escape codes parser"
license = "GPL-3.0-only"
url = "https://gitlab.com/saalen/ansifilter"
source = f"{url}/-/archive/{pkgver}/ansifilter-{pkgver}.tar.gz"
sha256 = "d3dd7503044c91c70e8b4c99489cb222cf831974bb7edc6b52acbd0a21742f50"
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
