pkgname = "gopls"
pkgver = "0.16.1"
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
sha256 = "0805bb9d3bfa51334b4d45a3182daea3e77ecbe27f4ddc672841ec72f63ed20a"
# debug: fails to split on powerpc
# check: regtest/marker fails with go1.22
options = ["!debug", "!check"]


def do_prepare(self):
    self.golang.mod_download(wrksrc=build_wrksrc)


def post_install(self):
    self.install_license("../LICENSE")
    self.install_license("../PATENTS")
    self.install_files("doc", "usr/share/doc/gopls")
