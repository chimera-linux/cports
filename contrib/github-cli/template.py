pkgname = "github-cli"
pkgver = "2.41.0"
pkgrel = 0
build_style = "go"
make_build_args = [
    f"-ldflags=-X github.com/cli/cli/v2/internal/build.Version=v{pkgver}",
    "./cmd/gh",
    "./cmd/gen-docs",
]
make_check_args = ["./..."]
hostmakedepends = ["go"]
checkdepends = ["git", "openssh"]
pkgdesc = "GitHub CLI tool"
maintainer = "triallax <triallax@tutanota.com>"
license = "MIT"
url = "https://cli.github.com"
source = f"https://github.com/cli/cli/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "bab15c4119f29e763355dd9a63b4e5824432b45834e5269353f3def6a27ccf80"
options = ["!cross", "!debug"]


def post_build(self):
    self.do("./build/gen-docs", "--man-page", "--doc-path", "man")

    with open(self.cwd / "gh.bash", "w") as cf:
        self.do("build/gh", "completion", "-s=bash", stdout=cf)

    with open(self.cwd / "gh.zsh", "w") as cf:
        self.do("build/gh", "completion", "-s=zsh", stdout=cf)

    with open(self.cwd / "gh.fish", "w") as cf:
        self.do("build/gh", "completion", "-s=fish", stdout=cf)


def do_install(self):
    # Don't use go build style install because it would also install gen-docs
    self.install_bin("build/gh")
    self.install_license("LICENSE")
    self.install_man("man/*.1", glob=True)

    self.install_completion("gh.bash", "bash")
    self.install_completion("gh.fish", "fish")
    self.install_completion("gh.zsh", "zsh")
