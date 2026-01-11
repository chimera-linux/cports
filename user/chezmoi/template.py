pkgname = "chezmoi"
pkgver = "2.69.1"
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
sha256 = "5237f42076d02e2d109149e7c2985cd28468027ea918232c6062f4897b23be56"
# may be disabled
options = []

if self.profile().arch in ["riscv64"]:
    # times out
    options += ["!check"]


def post_extract(self):
    # test needs network
    self.rm("internal/cmd/testdata/scripts/issue4647.txtar")


def check(self):
    from cbuild.util import golang

    self.do("make", "test", env=golang.get_go_env(self))


def post_install(self):
    self.install_license("LICENSE")

    with self.pushd("completions"):
        self.install_completion("chezmoi-completion.bash", "bash")
        self.install_completion("chezmoi.fish", "fish")
        self.install_completion("chezmoi.zsh", "zsh")
