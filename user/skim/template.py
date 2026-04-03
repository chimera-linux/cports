pkgname = "skim"
pkgver = "5.4.0"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "Fuzzy finder program"
license = "MIT"
url = "https://github.com/skim-rs/skim"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "f968750ddd453c031f6fec5164c0a1e24eb7c52639fe64f3b5bb657664f0e591"
# a bunch of integration tests fail due to layout etc
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
    self.install_man("man/man1/sk.1")
    self.install_file("plugin/skim.vim", "usr/share/vim/vimfiles/plugin")
    self.install_file("plugin/skim.vim", "usr/share/nvim/runtime/plugin")
    self.install_bin("bin/sk-tmux")
    self.install_man("man/man1/sk-tmux.1")

    self.install_completion("shell/completion.bash", "bash", name="sk")
    self.install_completion("shell/completion.fish", "fish", name="sk")
    self.install_completion("shell/completion.zsh", "zsh", name="sk")
    self.install_completion("shell/completion.nu", "nushell", name="sk")

    for ext in ["bash", "fish", "zsh"]:
        self.install_file(f"shell/key-bindings.{ext}", "usr/share/skim")


@subpackage("skim-tmux")
def _(self):
    self.subdesc = "tmux integration script"
    self.depends = [self.parent, "bash", "tmux"]
    self.install_if = [self.parent, "bash", "tmux"]

    return ["cmd:sk-tmux"]
