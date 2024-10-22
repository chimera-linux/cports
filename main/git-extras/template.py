pkgname = "git-extras"
pkgver = "7.3.0"
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
maintainer = "ttyyls <contact@behri.org>"
license = "MIT"
url = "https://github.com/tj/git-extras"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "89bae1a05731f4aaafb04066ea0186e181117b74fcfbf89d686cf205459220b7"


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
