pkgname = "coeurl"
pkgver = "0.3.1"
pkgrel = 2
build_style = "meson"
configure_args = ["-Dtests=true"]
hostmakedepends = [
    "cmake",
    "meson",
    "pkgconf",
]
makedepends = [
    "doctest",
    "curl-devel",
    "libevent-devel",
    "spdlog-devel",
]
pkgdesc = "Asynchronous libcurl wrapper"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "MIT"
url = "https://nheko.im/nheko-reborn/coeurl"
source = f"{url}/-/archive/v{pkgver}.tar.gz"
sha256 = "1e1b8cef13f526429918849c9dee0d18de815e82fccda29c540cc98b06efb7a9"
# need net
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")


@subpackage("coeurl-devel")
def _(self):
    return self.default_devel()
