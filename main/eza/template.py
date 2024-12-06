pkgname = "eza"
pkgver = "0.20.11"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable", "pkgconf"]
makedepends = [
    "libgit2-devel",
    "rust-std",
    "zlib-ng-compat-devel",
]
pkgdesc = "Directory listing utility"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "EUPL-1.2"
url = "https://eza.rocks"
source = (
    f"https://github.com/eza-community/eza/archive/refs/tags/v{pkgver}.tar.gz"
)
sha256 = "1a3ec9fb87c61e2369b46945ff1fafb7cbb5e6cb4693bb59003f4b628a93a04c"


def post_install(self):
    self.install_completion("completions/bash/eza", "bash")
    self.install_completion("completions/zsh/_eza", "zsh")
    self.install_completion("completions/fish/eza.fish", "fish")
