pkgname = "qhull"
pkgver = "2020.2"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DCMAKE_POLICY_VERSION_MINIMUM=3.5",
    "-DLINK_APPS_SHARED=ON",
]
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
]
pkgdesc = "Library for computing convex hulls"
license = "custom:qhull"
url = "http://www.qhull.org"
source = f"https://github.com/qhull/qhull/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "59356b229b768e6e2b09a701448bfa222c37b797a84f87f864f97462d8dbc7c5"


def post_install(self):
    self.install_license("COPYING.txt")


@subpackage("qhull-devel")
def _(self):
    return self.default_devel()


@subpackage("qhull-progs")
def _(self):
    return self.default_progs()
