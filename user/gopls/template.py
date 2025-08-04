pkgname = "gopls"
pkgver = "0.20.0"
pkgrel = 0
build_wrksrc = "gopls"
build_style = "go"
hostmakedepends = ["go"]
checkdepends = ["bash"]
pkgdesc = "Official Go language server"
license = "BSD-3-Clause"
url = "https://github.com/golang/tools/tree/master/gopls"
source = (
    f"https://github.com/golang/tools/archive/refs/tags/gopls/v{pkgver}.tar.gz"
)
sha256 = "1ff2a83be8be5a61b97fc5d72eab66f368ec20b52c513cc6656fc2e502e46f19"
# regtest/marker fails with go1.22
options = ["!check"]


def prepare(self):
    self.golang.mod_download(wrksrc=build_wrksrc)


def post_install(self):
    self.install_license("../LICENSE")
    self.install_license("../PATENTS")
    self.install_files("doc", "usr/share/doc/gopls")
