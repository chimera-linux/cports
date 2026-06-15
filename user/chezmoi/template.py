pkgname = "chezmoi"
pkgver = "2.70.5"
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
sha256 = "653b6585db407c92ab902304136fa4516263c4e7e6e84163a3c1a186b3ddf55f"
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
