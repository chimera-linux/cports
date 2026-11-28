pkgname = "fluxcd"
pkgver = "2.10.1"
pkgrel = 0
build_style = "go"
make_build_args = [
    f"-ldflags= -s -w -X main.VERSION={pkgver}",
    "./cmd/flux",
]
hostmakedepends = ["go", "bash"]
makedepends = ["kustomize"]
pkgdesc = "Open and extensible continuous delivery solution for Kubernetes"
license = "Apache-2.0"
url = "https://fluxcd.io"
source = f"https://github.com/fluxcd/flux2/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "c51e8faaaa57ecb517a8956800973ea39fd30b7a003a6eb3d25f88595ae1a093"


def post_extract(self):
    # remove tests that require network access
    self.rm("cmd/flux/create_secret_git_test.go")
    self.rm("pkg/manifestgen/install/install_test.go")


def post_prepare(self):
    # build manifests using kustomize
    self.do("./manifests/scripts/bundle.sh", allow_network=True)


def post_build(self):
    for shell in ["bash", "fish", "zsh"]:
        with open(self.cwd / f"flux.{shell}", "w") as outf:
            self.do("build/flux", "completion", shell, stdout=outf)


def post_install(self):
    for shell in ["bash", "fish", "zsh"]:
        self.install_completion(f"flux.{shell}", shell, name="flux")
