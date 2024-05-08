pkgname = "age"
pkgver = "1.1.1"
pkgrel = 2
build_style = "go"
make_build_args = [f"-ldflags=-X main.Version={pkgver}", "./cmd/..."]
hostmakedepends = ["go"]
pkgdesc = "File encryption tool"
maintainer = "psykose <alice@ayaya.dev>"
license = "BSD-3-Clause"
url = "https://github.com/FiloSottile/age"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "f1f3dbade631976701cd295aa89308681318d73118f5673cced13f127a91178c"
# tests invoke network downloads for vectors
options = ["!debug", "!check"]


def post_install(self):
    self.install_man("doc/*.1", glob=True)
    self.install_license("LICENSE")
