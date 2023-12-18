pkgname = "conmon"
pkgver = "2.1.9"
pkgrel = 1
build_style = "meson"
hostmakedepends = [
    "go-md2man",
    "meson",
    "pkgconf",
]
makedepends = [
    "glib-devel",
    "libseccomp-devel",
    "linux-headers",
]
pkgdesc = "OCI container monitor"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Apache-2.0"
url = "https://github.com/containers/conmon"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "15a41e78f5e86dba429cc78ef4836f44ba927b6c69f1cd1721118a08ca0fd1f5"


def post_build(self):
    self.do("go-md2man", "-in", "docs/conmon.8.md", "-out", "docs/conmon.8")


def post_install(self):
    self.install_man("docs/conmon.8")
