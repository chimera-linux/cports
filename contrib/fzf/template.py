pkgname = "fzf"
pkgver = "0.54.2"
pkgrel = 1
build_style = "go"
hostmakedepends = ["go"]
makedepends = ["ncurses-devel"]
pkgdesc = "Command-line fuzzy finder"
maintainer = "Wesley Moore <wes@wezm.net>"
license = "MIT"
url = "https://github.com/junegunn/fzf"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "2f4f7bbe2bfbe1eb24ab86fc2a5d93a1f55c33aaca9fe39495af0128712ca81f"


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
