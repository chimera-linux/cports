pkgname = "glab"
pkgver = "1.124.0"
pkgrel = 0
build_style = "go"
prepare_after_patch = True
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
sha256 = "89042f881c50f14fca83d504d4c7999f59daa6d29557dea3a882514e3dcea3bb"
# check may be disabled
options = ["!cross"]

if self.profile.arch not in ["aarch64", "x86_64"]:
    # some tests are platform-specific
    options += ["!check"]


def post_extract(self):
    self.rm("vendor", recursive=True)


def post_prepare(self):
    self.do(
        "go",
        "run",
        "./cmd/gen-docs/docs.go",
        "--manpage",
        "--path",
        "./share/man/man1",
        allow_network=True,
    )


def post_build(self):
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
