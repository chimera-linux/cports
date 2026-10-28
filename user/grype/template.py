pkgname = "grype"
pkgver = "0.121.0"
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
sha256 = "87244bc41b3fbd596d12f31f2f0e335d36c1059662f27baa31036584e427d169"
hardening = []
# Test suite depends on docker
# generates manpages/completions with host bins
options = ["!check", "!cross"]

match self.profile.arch:
    case "ppc64le" | "ppc64":
        # https://github.com/golang/go/issues/82324
        hardening += ["!pie"]


def post_build(self):
    for shell in ["bash", "fish", "zsh"]:
        with open(self.cwd / f"grype.{shell}", "w") as outf:
            self.do("build/grype", "completion", shell, stdout=outf)


def post_install(self):
    for shell in ["bash", "fish", "zsh"]:
        self.install_completion(f"grype.{shell}", shell)
