pkgname = "neocmakelsp"
pkgver = "0.8.22"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "CMake language server"
license = "MIT"
url = "https://neocmakelsp.github.io"
source = f"https://github.com/neocmakelsp/neocmakelsp/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "ec6c505fd74b5160c29e6c52bba4c5835f5456bf39983c105bccf0b0622bc72b"


def post_install(self):
    self.install_license("LICENSE")
    self.install_completion("completions/bash/neocmakelsp", "bash")
    self.install_completion("completions/fish/neocmakelsp.fish", "fish")
    self.install_completion("completions/zsh/_neocmakelsp", "zsh")
