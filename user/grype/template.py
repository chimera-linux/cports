pkgname = "grype"
pkgver = "0.117.0"
pkgrel = 0
build_style = "go"
make_build_args = [
    f"-ldflags= -X main.version={pkgver}",
    "./cmd/grype",
]
hostmakedepends = ["go"]
pkgdesc = "Vulnerability scanner for container images and filesystems"
license = "Apache-2.0"
url = "https://github.com/anchore/grype"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "314a955453e4f69b3cee1a1982eed8e779ff8ae70e017d37a211d734b9083a94"
# Test suite depends on docker
# generates manpages/completions with host bins
options = ["!check", "!cross"]


def post_build(self):
    for shell in ["bash", "fish", "zsh"]:
        with open(self.cwd / f"grype.{shell}", "w") as outf:
            self.do("build/grype", "completion", shell, stdout=outf)


def post_install(self):
    for shell in ["bash", "fish", "zsh"]:
        self.install_completion(f"grype.{shell}", shell)
