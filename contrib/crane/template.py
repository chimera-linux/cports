pkgname = "crane"
pkgver = "0.20.1"
pkgrel = 0
build_style = "go"
make_build_args = ["./cmd/crane"]
hostmakedepends = ["go"]
pkgdesc = "Container image and registry manipulation tool"
maintainer = "Radosław Piliszek <radek@piliszek.it>"
license = "Apache-2.0"
url = "https://github.com/google/go-containerregistry"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "4bae53f34011e35ef874a60123b8ae70a5e992d804decb030479dbb888afe6d1"


# docs are present but they do not render properly as manpages
# and so they are skipped here
def post_build(self):
    for shell in ["bash", "fish", "zsh"]:
        with open(self.cwd / f"crane.{shell}comp", "w") as cf:
            self.do(f"{self.make_dir}/crane", "completion", shell, stdout=cf)


def pre_check(self):
    # This particular test is marked broken on arm64 and darwin.
    # It seems it is also broken on linux-musl.
    self.do("rm", "pkg/v1/google/auth_test.go")


def post_install(self):
    for shell in ["bash", "fish", "zsh"]:
        self.install_completion(f"crane.{shell}comp", shell=shell)
