pkgname = "chezmoi"
pkgver = "2.63.1"
pkgrel = 0
build_style = "go"
make_build_args = [
    f"-ldflags=-X main.version={pkgver} -X 'main.builtBy=Chimera Linux'",
]
hostmakedepends = ["go"]
checkdepends = ["gnupg", "git"]
go_build_tags = ["noembeddocs", "noupgrade"]
pkgdesc = "Dotfiles manager"
license = "MIT"
url = "https://chezmoi.io"
source = f"https://github.com/twpayne/chezmoi/archive/v{pkgver}.tar.gz"
sha256 = "cae49bb1abef58acfc471681cca6d189ab1d0e9d1590e0905c12d3a32bc23014"
# may be disabled
options = []

if self.profile().arch in ["riscv64"]:
    # times out
    options += ["!check"]


def check(self):
    from cbuild.util import golang

    self.do("make", "test", env=golang.get_go_env(self))


def post_install(self):
    self.install_license("LICENSE")

    with self.pushd("completions"):
        self.install_completion("chezmoi-completion.bash", "bash")
        self.install_completion("chezmoi.fish", "fish")
        self.install_completion("chezmoi.zsh", "zsh")
