pkgname = "conmon"
pkgver = "2.2.1"
pkgrel = 0
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
license = "Apache-2.0"
url = "https://github.com/containers/conmon"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "814fb5979a3a4b8576b1f901e606b482bebb41cb7e57926e6d5765ee786b96d3"


def post_build(self):
    self.do("go-md2man", "-in", "docs/conmon.8.md", "-out", "docs/conmon.8")


def post_install(self):
    self.install_man("docs/conmon.8")
