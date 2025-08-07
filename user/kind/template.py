pkgname = "kind"
pkgver = "0.27.0"
pkgrel = 6
build_style = "go"
make_check_args = ["-skip", "TestIntegrationEnsureNetworkConcurrent"]
hostmakedepends = ["go"]
pkgdesc = "Containerized Kubernetes Environment in Docker"
license = "Apache-2.0"
url = "https://kind.sigs.k8s.io"
source = f"https://github.com/kubernetes-sigs/kind/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "841dd2fdc5c194e1ea49f36204cce33a943285862303713a1baa5d2073cdb0d9"
# cross: uses host binary to generate completions
options = ["!cross"]


def post_build(self):
    for completion in ["bash", "fish", "zsh"]:
        with open(f"{self.cwd}/kind.{completion}", "w") as o:
            self.do("build/kind", "completion", completion, stdout=o)


def post_install(self):
    for completion in ["bash", "fish", "zsh"]:
        self.install_completion(f"kind.{completion}", completion)
