pkgname = "crane"
pkgver = "0.20.2"
pkgrel = 1
build_style = "go"
make_build_args = ["./cmd/crane"]
hostmakedepends = ["go"]
pkgdesc = "Container image and registry manipulation tool"
maintainer = "Radosław Piliszek <radek@piliszek.it>"
license = "Apache-2.0"
url = "https://github.com/google/go-containerregistry"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "064e9c47e3dac49acddccb4afe908b9d835725d371ee9a471fd445d134fbbf1d"


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
