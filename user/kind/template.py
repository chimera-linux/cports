pkgname = "kind"
pkgver = "0.25.0"
pkgrel = 0
build_style = "go"
make_check_args = ["-skip", "TestIntegrationEnsureNetworkConcurrent"]
hostmakedepends = ["go"]
pkgdesc = "Containerized Kubernetes Environment in Docker"
maintainer = "tulilirockz <tulilirockz@outlook.com>"
license = "Apache-2.0"
url = "https://kind.sigs.k8s.io"
source = f"https://github.com/kubernetes-sigs/kind/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "016c36750be5c5fb81f70e4675ee0a4f278dd929f05273184ff68cae112ce71b"
# cross: uses host binary to generate completions
options = ["!cross"]


def post_build(self):
    for completion in ["bash", "fish", "zsh"]:
        with open(f"{self.cwd}/kind.{completion}", "w") as o:
            self.do("build/kind", "completion", completion, stdout=o)


def post_install(self):
    for completion in ["bash", "fish", "zsh"]:
        self.install_completion(f"kind.{completion}", completion)
