pkgname = "crane"
pkgver = "0.20.6"
pkgrel = 2
build_style = "go"
make_build_args = ["./cmd/crane"]
hostmakedepends = ["go"]
pkgdesc = "Container image and registry manipulation tool"
license = "Apache-2.0"
url = "https://github.com/google/go-containerregistry"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "53f17964ade63f63b2c66231a6e1ea606345cfcc325e49a5267017bb475bdcb4"
# cross: generates completions with host binary
options = ["!cross"]


def post_extract(self):
    # marked broken on arm64/darwin; apparently also on musl in general
    self.rm("pkg/v1/google/auth_test.go")


# docs are present but they do not render properly as manpages
# and so they are skipped here
def post_build(self):
    for shell in ["bash", "fish", "zsh"]:
        with open(self.cwd / f"crane.{shell}comp", "w") as cf:
            self.do(f"{self.make_dir}/crane", "completion", shell, stdout=cf)


def post_install(self):
    for shell in ["bash", "fish", "zsh"]:
        self.install_completion(f"crane.{shell}comp", shell=shell)
