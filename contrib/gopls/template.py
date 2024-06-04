pkgname = "gopls"
pkgver = "0.15.3"
pkgrel = 2
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
sha256 = "7fb0a43ff5e562089ca0ec3e8e7819dd205977758c02ea9bded05f56d5080a54"
# debug: fails to split on powerpc
# check: regtest/marker fails with go1.22
options = ["!debug", "!check"]


def do_prepare(self):
    self.golang.mod_download(wrksrc=build_wrksrc)


def post_install(self):
    self.install_license("../LICENSE")
    self.install_license("../PATENTS")
    self.install_files("doc", "usr/share/doc/gopls")
