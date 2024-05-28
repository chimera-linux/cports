pkgname = "just"
pkgver = "1.27.0"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
checkdepends = ["bash", "python"]
pkgdesc = "Save and run commands from justfile"
maintainer = "Wesley Moore <wes@wezm.net>"
license = "CC0-1.0"
url = "https://github.com/casey/just"
source = f"{url}/archive/{pkgver}.tar.gz"
sha256 = "3f7af44ce43fef5e54df2b64574930e036baadae4a66645e996c4bb2164bf2a3"


def post_install(self):
    self.install_man("man/just.1")
    self.install_completion("completions/just.bash", "bash")
    self.install_completion("completions/just.zsh", "zsh")
    self.install_completion("completions/just.fish", "fish")
