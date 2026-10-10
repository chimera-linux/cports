pkgname = "hayagriva"
pkgver = "0.10.1"
pkgrel = 0
build_style = "cargo"
make_build_args = ["--features=cli,csl-json"]
hostmakedepends = ["cargo-auditable"]
pkgdesc = "Tool for querying, formatting and converting bibliographies"
license = "(Apache-2.0 OR MIT) AND CC-BY-SA-3.0"
url = "https://github.com/typst/hayagriva"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "bce8393f5200a3672b0d5baade84cfd96646dc7f0e045faedb0bf9a754c1a48d"


def install(self):
    from cbuild.util import cargo

    self.install_bin(cargo.target_path(self, "hayagriva"))
    self.install_license("LICENSE-MIT")
    self.install_license("NOTICE")
