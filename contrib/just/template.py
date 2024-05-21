pkgname = "just"
pkgver = "1.26.0"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
checkdepends = ["bash"]
pkgdesc = "Save and run commands from justfile"
maintainer = "Wesley Moore <wes@wezm.net>"
license = "CC0-1.0"
url = "https://github.com/casey/just"
source = f"{url}/archive/{pkgver}.tar.gz"
sha256 = "20c4109bf30590e5633ae005329508c3fa772c3d86d0994bd2f770ade02dd6a7"


def post_install(self):
    self.install_man("man/just.1")
    self.install_completion("completions/just.bash", "bash")
    self.install_completion("completions/just.zsh", "zsh")
    self.install_completion("completions/just.fish", "fish")
