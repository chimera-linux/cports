pkgname = "sk"
pkgver = "4.6.2"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "Fuzzy Finder in rust!"
license = "MIT"
url = "https://github.com/skim-rs/skim"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
source_paths = ["."]
sha256 = "bb74eb7f9751f7c43fd634c5714f612eae67830db852e74c01a4d83da8086e3c"


def post_install(self):
    self.install_license("LICENSE")
    self.install_man("man/man1/sk.1")
    self.install_file("plugin/skim.vim", "usr/share/vim/vimfiles/plugin")
    self.install_file("plugin/skim.vim", "usr/share/nvim/runtime/plugin")
    self.install_bin("bin/sk-tmux")
    self.install_man("man/man1/sk-tmux.1")

    with self.pushd("shell"):
        self.install_completion("completion.bash", "bash")
        self.install_completion("completion.fish", "fish")
        self.install_completion("completion.zsh", "zsh")
        self.install_completion("completion.nu", "nushell")

        for ext in ["bash", "fish", "zsh"]:
            self.install_file(f"key-bindings.{ext}", "usr/share/sk")


@subpackage("sk-tmux")
def _(self):
    self.subdesc = "tmux integration script"
    self.depends = [self.parent, "bash", "tmux"]
    self.install_if = [self.parent, "bash", "tmux"]

    return ["cmd:sk-tmux"]
