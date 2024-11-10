pkgname = "fzf"
pkgver = "0.56.1"
pkgrel = 0
build_style = "go"
hostmakedepends = ["go"]
makedepends = ["ncurses-devel"]
pkgdesc = "Command-line fuzzy finder"
maintainer = "Wesley Moore <wes@wezm.net>"
license = "MIT"
url = "https://github.com/junegunn/fzf"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "799c558628462fe0767ca282ed7e0746633239b80ab09ebc9d6f3653e3b788c9"


def post_install(self):
    self.install_license("LICENSE")
    self.install_man("man/man1/fzf.1")
    self.install_file("plugin/fzf.vim", "usr/share/vim/vimfiles/plugin")
    self.install_file("plugin/fzf.vim", "usr/share/nvim/runtime/plugin")
    self.install_bin("bin/fzf-tmux")
    self.install_man("man/man1/fzf-tmux.1")

    with self.pushd("shell"):
        self.install_completion("completion.bash", "bash")
        self.install_completion("completion.zsh", "zsh")

        for ext in ["bash", "fish", "zsh"]:
            self.install_file(f"key-bindings.{ext}", "usr/share/fzf")


@subpackage("fzf-tmux")
def _(self):
    self.subdesc = "tmux integration script"
    self.depends = [self.parent, "bash", "tmux"]
    self.install_if = [self.parent, "bash", "tmux"]

    return ["cmd:fzf-tmux"]
