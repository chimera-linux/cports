pkgname = "conmon"
pkgver = "2.1.8"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "pkgconf", "go-md2man"]
makedepends = ["linux-headers", "libseccomp-devel", "glib-devel"]
depends = ["libseccomp", "crun"]
pkgdesc = "OCI container runtime monitor"
maintainer = "roastveg <louis@hamptonsoftworks.com>"
license = "Apache-2.0"
url = "https://github.com/containers/conmon"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "e72c090210a03ca3b43a0fad53f15bca90bbee65105c412468009cf3a5988325"


def post_build(self):
    self.do("go-md2man", "-in", "docs/conmon.8.md", "-out", "docs/conmon.8")


def post_install(self):
    self.install_man("docs/conmon.8")
