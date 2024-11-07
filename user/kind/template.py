pkgname = "kind"
pkgver = "0.24.0"
pkgrel = 1
build_style = "go"
make_check_args = ["-skip", "TestIntegrationEnsureNetworkConcurrent"]
hostmakedepends = ["go"]
pkgdesc = "Containerized Kubernetes Environment in Docker"
maintainer = "tulilirockz <tulilirockz@outlook.com>"
license = "Apache-2.0"
url = "https://kind.sigs.k8s.io"
source = f"https://github.com/kubernetes-sigs/kind/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "eb7bcb8005ff980d7d7ad088165a5a6236f484444aa397520cd98cb046e1d797"
# cross: uses host binary to generate completions
options = ["!cross"]


def post_build(self):
    for completion in ["bash", "fish", "zsh"]:
        with open(f"{self.cwd}/kind.{completion}", "w") as o:
            self.do("build/kind", "completion", completion, stdout=o)


def post_install(self):
    for completion in ["bash", "fish", "zsh"]:
        self.install_completion(f"kind.{completion}", completion)
