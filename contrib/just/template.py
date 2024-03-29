pkgname = "just"
pkgver = "1.25.2"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo"]
makedepends = ["rust-std"]
checkdepends = ["bash"]
pkgdesc = "Save and run commands from justfile"
maintainer = "Wesley Moore <wes@wezm.net>"
license = "CC0-1.0"
url = "https://github.com/casey/just"
source = f"{url}/archive/{pkgver}.tar.gz"
sha256 = "5a005a4de9f99b297ba7b5dc02c3365c689e579148790660384afee0810a2342"


def post_install(self):
    self.install_man("man/just.1")
    self.install_completion("completions/just.bash", "bash")
    self.install_completion("completions/just.zsh", "zsh")
    self.install_completion("completions/just.fish", "fish")
