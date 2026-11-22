pkgname = "hyperfine"
pkgver = "2.0.0"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "Command-line benchmarking tool"
license = "MIT OR Apache-2.0"
url = "https://github.com/sharkdp/hyperfine"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "f4b71df3c78e4cf752ca6fb6ebc4b025f7ea6a5ca5c48fea75f8a1fdb4c7d721"


def install(self):
    from cbuild.util import cargo

    self.install_bin(cargo.target_path(self, "hyperfine"))
    self.install_man("doc/hyperfine.1")
    self.install_license("LICENSE-MIT")
    self.install_completion(
        next(self.find("target/", "hyperfine.bash")), "bash"
    )
    self.install_completion(next(self.find("target/", "_hyperfine")), "zsh")
    self.install_completion(
        next(self.find("target/", "hyperfine.fish")), "fish"
    )
