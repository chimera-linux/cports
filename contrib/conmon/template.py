pkgname = "conmon"
pkgver = "2.1.12"
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
maintainer = "q66 <q66@chimera-linux.org>"
license = "Apache-2.0"
url = "https://github.com/containers/conmon"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "842f0b5614281f7e35eec2a4e35f9f7b9834819aa58ecdad8d0ff6a84f6796a6"


def post_build(self):
    self.do("go-md2man", "-in", "docs/conmon.8.md", "-out", "docs/conmon.8")


def post_install(self):
    self.install_man("docs/conmon.8")
