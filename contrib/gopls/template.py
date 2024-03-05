pkgname = "gopls"
pkgver = "0.14.2"
pkgrel = 1
build_wrksrc = "gopls"
build_style = "go"
hostmakedepends = ["go"]
checkdepends = ["bash"]
pkgdesc = "Official Go language server"
maintainer = "triallax <triallax@tutanota.com>"
license = "BSD-3-Clause"
url = "https://github.com/golang/tools/tree/master/gopls"
source = (
    f"https://github.com/golang/tools/archive/refs/tags/gopls/v{pkgver}.tar.gz"
)
sha256 = "5a4939e08adf4de0720042868b43405de0cf221ae9a0b266694d4f222b3edfbb"
# debug: fails to split on powerpc
# check: regtest/marker fails with go1.22
options = ["!debug", "!check"]


def do_prepare(self):
    self.golang.mod_download(wrksrc=build_wrksrc)


def post_install(self):
    self.install_license("../LICENSE")
    self.install_license("../PATENTS")
    self.install_files("doc", "usr/share/doc/gopls")
