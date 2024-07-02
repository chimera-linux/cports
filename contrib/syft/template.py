pkgname = "syft"
pkgver = "1.4.1"
pkgrel = 2
build_style = "go"
make_build_args = [
    f"-ldflags= -X main.version={pkgver}",
    "./cmd/syft",
]
hostmakedepends = ["go"]
pkgdesc = "SBOM generator CLI for container images, filesystems and binaries"
maintainer = "Jan Christian Grünhage <jan.christian@gruenhage.xyz>"
license = "Apache-2.0"
url = "https://github.com/anchore/syft"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "822808af90626929dd7725df511a674386303482a1ddd316345066e6de09b157"
# Test suite depends on docker
# generates manpages/completions with host bins
options = ["!check", "!cross"]


def post_build(self):
    for shell in ["bash", "fish", "zsh"]:
        with open(self.cwd / f"syft.{shell}", "w") as outf:
            self.do("build/syft", "completion", shell, stdout=outf)


def post_install(self):
    for shell in ["bash", "fish", "zsh"]:
        self.install_completion(f"syft.{shell}", shell)
