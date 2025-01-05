pkgname = "kind"
pkgver = "0.26.0"
pkgrel = 0
build_style = "go"
make_check_args = ["-skip", "TestIntegrationEnsureNetworkConcurrent"]
hostmakedepends = ["go"]
pkgdesc = "Containerized Kubernetes Environment in Docker"
maintainer = "Gabriel M. Dutra <dmdutra@proton.me>"
license = "Apache-2.0"
url = "https://kind.sigs.k8s.io"
source = f"https://github.com/kubernetes-sigs/kind/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "6b0ae7748144034ba296a302f5aaaad7120aef4df9d8138cc6276a43ca3c96d1"
# cross: uses host binary to generate completions
options = ["!cross"]


def post_build(self):
    for completion in ["bash", "fish", "zsh"]:
        with open(f"{self.cwd}/kind.{completion}", "w") as o:
            self.do("build/kind", "completion", completion, stdout=o)


def post_install(self):
    for completion in ["bash", "fish", "zsh"]:
        self.install_completion(f"kind.{completion}", completion)
