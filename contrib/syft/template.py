pkgname = "syft"
pkgver = "1.0.1"
pkgrel = 0
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
sha256 = "79852b27a0665da4e41139066c009aaeae488e82fd6b465129aed5734c5ac934"
# Test suite depends on docker
# generates manpages/completions with host bins
options = ["!check", "!cross"]


def post_build(self):
    self.do("sh", "-c", "build/syft completion bash > syft.bash")
    self.do("sh", "-c", "build/syft completion fish > syft.fish")
    self.do("sh", "-c", "build/syft completion zsh > _syft")


def post_install(self):
    self.install_completion("syft.bash", "bash")
    self.install_completion("syft.fish", "fish")
    self.install_completion("_syft", "zsh")
