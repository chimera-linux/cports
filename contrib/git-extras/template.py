pkgname = "git-extras"
pkgver = "7.2.0"
pkgrel = 1
build_style = "makefile"
make_install_args = [
    "COMPL_DIR=$(DESTDIR)/usr/share/bash-completion/completions"
]
make_check_target = "test"
hostmakedepends = ["bash"]
depends = ["bash", "git"]
checkdepends = ["git", "python-gitpython", "python-pytest", "python-testpath"]
pkgdesc = "Extra Git utilities"
maintainer = "ttyyls <contact@behri.org>"
license = "MIT"
url = "https://github.com/tj/git-extras"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "f570f19b9e3407e909cb98d0536c6e0b54987404a0a053903a54b81680c347f1"


def build(self):
    pass


def post_install(self):
    self.install_license("LICENSE")
    # this package's fish and zsh completions bundle up completions for all
    # commands into one file instead of a separate file for each command, and
    # since fish/zsh use the completion filename to load completions on-demand,
    # they don't get autoloaded correctly; therefore, don't use
    # install_completion for them
    self.install_file(
        "etc/git-extras-completion.zsh",
        "usr/share/git-extras",
        name="completions.zsh",
    )
    self.install_file(
        "etc/git-extras.fish", "usr/share/git-extras", name="completions.fish"
    )
