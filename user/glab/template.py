pkgname = "glab"
pkgver = "1.123.0"
pkgrel = 0
build_style = "go"
make_build_args = [
    "-ldflags",
    f"-X main.commit=v{pkgver} -X main.version={pkgver}",
    "gitlab.com/gitlab-org/cli/cmd/glab",
]
make_check_args = ["-skip", "TestIsTelemetryEnabled", "./..."]
hostmakedepends = ["go"]
checkdepends = ["git"]
depends = ["git"]
pkgdesc = "Command-line frontend to interact with GitLab"
license = "MIT"
url = "https://gitlab.com/gitlab-org/cli"
source = f"{url}/-/releases/v{pkgver}/downloads/glab_{pkgver}_source.tar.gz"
sha256 = "d36ed66164dd1491a40182a3f9d40d187fd239b8d7e54c3751c7b2bb29d9193a"
# check may be disabled
options = ["!cross"]

if self.profile.arch not in ["aarch64", "x86_64"]:
    # some tests are platform-specific
    options += ["!check"]


def post_build(self):
    self.do(
        "go",
        "run",
        "./cmd/gen-docs/docs.go",
        "--manpage",
        "--path",
        "./share/man/man1",
    )
    for shell in ["bash", "fish", "zsh"]:
        with open(self.cwd / f"glab.{shell}", "w") as outf:
            self.do("build/glab", "completion", "--shell", shell, stdout=outf)


def pre_check(self):
    # glab test requires the source root to be a git directory
    self.do("git", "init", "-b", "master")


def post_install(self):
    self.install_license("LICENSE")
    self.install_man("share/man/man1/*", glob=True)
    for shell in ["bash", "fish", "zsh"]:
        self.install_completion(f"glab.{shell}", shell)
