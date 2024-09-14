pkgname = "typst-lsp"
pkgver = "0.13.0"
pkgrel = 0
build_style = "cargo"
make_build_args = [
    "--no-default-features",
    "--features=remote-packages,fontconfig,native-tls",
]
make_check_args = [
    *make_build_args,
    "--",
    "--skip=workspace::package::external::remote_repo::test::full_download",
]
hostmakedepends = ["cargo-auditable", "pkgconf"]
makedepends = ["rust-std", "openssl-devel"]
pkgdesc = "Language server for typst"
maintainer = "ttyyls <contact@behri.org>"
license = "Apache-2.0 OR MIT"
url = "https://github.com/nvarner/typst-lsp"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "860d56653b719402736b00ac9bc09e5e418dea2577cead30644252e85ab5d1a1"


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/typst-lsp")
    self.install_license("LICENSE-MIT.txt")
