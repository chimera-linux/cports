pkgname = "fzf"
pkgver = "0.54.0"
pkgrel = 0
build_style = "go"
hostmakedepends = ["go"]
makedepends = ["ncurses-devel"]
pkgdesc = "Command-line fuzzy finder"
maintainer = "Wesley Moore <wes@wezm.net>"
license = "MIT"
url = "https://github.com/junegunn/fzf"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "ce658b153254e25cf4244365d639cf3ac5b91230a20f76bd6845d88e1267a2db"
# debug: fails to split on powerpc
options = ["!debug"]


def post_install(self):
    self.install_license("LICENSE")
    self.install_man("man/man1/fzf.1")
    self.install_file("plugin/fzf.vim", "usr/share/vim/vimfiles/plugin")
    self.install_file("plugin/fzf.vim", "usr/share/nvim/runtime/plugin")

    with self.pushd("shell"):
        self.install_completion("completion.bash", "bash")
        self.install_completion("completion.zsh", "zsh")
        for ext in ["bash", "fish", "zsh"]:
            self.install_file(f"key-bindings.{ext}", "usr/share/fzf")
