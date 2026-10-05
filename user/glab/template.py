pkgname = "glab"
pkgver = "1.120.0"
pkgrel = 0
build_style = "go"
make_build_args = [
    "-ldflags",
    f"-X main.commit=v{pkgver} -X main.version={pkgver}",
    "gitlab.com/gitlab-org/cli/cmd/glab",
]
hostmakedepends = ["go"]
checkdepends = ["git"]
depends = ["git"]
pkgdesc = "Command-line frontend to interact with GitLab"
license = "MIT"
url = "https://gitlab.com/gitlab-org/cli"
source = f"{url}/-/releases/v{pkgver}/downloads/glab_{pkgver}_source.tar.gz"
sha256 = "7a3e501a83f27b567432cc932ca99a31af46ee1ab6a9c0839e96e7fbc6bad55a"
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


def pre_check(self):
    # glab test requires the source root to be a git directory
    self.do("git", "init", "-b", "master")


def post_install(self):
    self.install_license("LICENSE")
    self.install_man("share/man/man1/*", glob=True)
