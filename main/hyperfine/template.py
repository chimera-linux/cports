pkgname = "hyperfine"
pkgver = "1.20.0"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "Command-line benchmarking tool"
license = "MIT OR Apache-2.0"
url = "https://github.com/sharkdp/hyperfine"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "f90c3b096af568438be7da52336784635a962c9822f10f98e5ad11ae8c7f5c64"


def post_install(self):
    self.install_man("doc/hyperfine.1")
    self.install_license("LICENSE-MIT")
    self.install_completion(
        next(self.find("target/", "hyperfine.bash")), "bash"
    )
    self.install_completion(next(self.find("target/", "_hyperfine")), "zsh")
    self.install_completion(
        next(self.find("target/", "hyperfine.fish")), "fish"
    )
