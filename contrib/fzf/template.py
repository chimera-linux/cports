pkgname = "fzf"
pkgver = "0.54.3"
pkgrel = 1
build_style = "go"
hostmakedepends = ["go"]
makedepends = ["ncurses-devel"]
pkgdesc = "Command-line fuzzy finder"
maintainer = "Wesley Moore <wes@wezm.net>"
license = "MIT"
url = "https://github.com/junegunn/fzf"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "6413f3916f8058b396820f9078b1336d94c72cbae39c593b1d16b83fcc4fdf74"


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
