pkgname = "fzf"
pkgver = "0.46.0"
pkgrel = 0
build_style = "go"
hostmakedepends = ["go"]
makedepends = ["ncurses-devel"]
pkgdesc = "Command-line fuzzy finder"
maintainer = "Wesley Moore <wes@wezm.net>"
license = "MIT"
url = "https://github.com/junegunn/fzf"
source = f"{url}/archive/{pkgver}.tar.gz"
sha256 = "56d0ecaaff90dd33c371f7d23d1fd1cb36eb42554e88284c2781a067fba2a645"
options = ["!strip"]


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
