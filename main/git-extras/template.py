pkgname = "git-extras"
pkgver = "7.4.0"
pkgrel = 0
build_style = "makefile"
make_install_args = [
    "COMPL_DIR=$(DESTDIR)/usr/share/bash-completion/completions"
]
make_check_target = "test"
hostmakedepends = ["bash"]
depends = ["bash", "git"]
checkdepends = ["git", "python-gitpython", "python-pytest", "python-testpath"]
pkgdesc = "Extra Git utilities"
license = "MIT"
url = "https://github.com/tj/git-extras"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "aaab3bab18709ec6825a875961e18a00e0c7d8214c39d6e3a63aeb99fa11c56e"


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
