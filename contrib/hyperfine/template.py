pkgname = "hyperfine"
pkgver = "1.17.0"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo"]
makedepends = ["rust"]
pkgdesc = "Command-line benchmarking tool"
maintainer = "psykose <alice@ayaya.dev>"
license = "MIT OR Apache-2.0"
url = "https://github.com/sharkdp/hyperfine"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "3dcd86c12e96ab5808d5c9f3cec0fcc04192a87833ff009063c4a491d5487b58"


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
