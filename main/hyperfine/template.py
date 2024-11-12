pkgname = "hyperfine"
pkgver = "1.19.0"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "Command-line benchmarking tool"
maintainer = "psykose <alice@ayaya.dev>"
license = "MIT OR Apache-2.0"
url = "https://github.com/sharkdp/hyperfine"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "d1c782a54b9ebcdc1dedf8356a25ee11e11099a664a7d9413fdd3742138fa140"


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
