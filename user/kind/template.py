pkgname = "kind"
pkgver = "0.31.0"
pkgrel = 1
build_style = "go"
make_check_args = ["-skip", "TestIntegrationEnsureNetworkConcurrent"]
hostmakedepends = ["go"]
pkgdesc = "Containerized Kubernetes Environment in Docker"
license = "Apache-2.0"
url = "https://kind.sigs.k8s.io"
source = f"https://github.com/kubernetes-sigs/kind/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "f4aaa1f572f9965eea3f7513d166f545f41b61ab5efeed953048bdcb13c51032"
# cross: uses host binary to generate completions
options = ["!cross"]


def post_build(self):
    for completion in ["bash", "fish", "zsh"]:
        with open(f"{self.cwd}/kind.{completion}", "w") as o:
            self.do("build/kind", "completion", completion, stdout=o)


def post_install(self):
    for completion in ["bash", "fish", "zsh"]:
        self.install_completion(f"kind.{completion}", completion)
