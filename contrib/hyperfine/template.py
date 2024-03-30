pkgname = "hyperfine"
pkgver = "1.18.0"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "Command-line benchmarking tool"
maintainer = "psykose <alice@ayaya.dev>"
license = "MIT OR Apache-2.0"
url = "https://github.com/sharkdp/hyperfine"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "fea7b92922117ed04b9c84bb9998026264346768804f66baa40743c5528bed6b"


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
