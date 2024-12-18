pkgname = "gopls"
pkgver = "0.17.0"
pkgrel = 0
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
sha256 = "0d362528c42d4110933515cbabd7c6383048eb279a0b74a6322883acbcc3a381"
# regtest/marker fails with go1.22
options = ["!check"]


def prepare(self):
    self.golang.mod_download(wrksrc=build_wrksrc)


def post_install(self):
    self.install_license("../LICENSE")
    self.install_license("../PATENTS")
    self.install_files("doc", "usr/share/doc/gopls")
