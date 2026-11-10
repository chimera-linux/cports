pkgname = "nerdctl"
pkgver = "2.4.2"
pkgrel = 0
build_style = "go"
make_build_args = [
    (
        "-ldflags="
        f"-X github.com/containerd/nerdctl/v2/pkg/version.Version=v{pkgver} "
        f"-X github.com/containerd/nerdctl/v2/pkg/version.Revision=chimera-r{pkgrel}"
    ),
    "./cmd/nerdctl",
]
hostmakedepends = ["go"]
depends = ["containerd", "iptables"]
pkgdesc = "Containerd CLI"
license = "Apache-2.0"
url = "https://github.com/containerd/nerdctl"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "f73026262a1cab7b6a8f3df66da54dbe52268184359c41408468d9b75d3b41d8"
hardening = []
# can't run tests inside namespaces
# cross: generates completions with host binary
options = ["!check", "!cross"]

if self.profile.arch == "ppc64le":
    # https://github.com/golang/go/issues/82324
    hardening += ["!pie"]


def post_build(self):
    for shell in ["bash", "fish", "zsh"]:
        with open(self.cwd / f"nerdctl.{shell}", "w") as f:
            self.do(f"{self.make_dir}/nerdctl", "completion", shell, stdout=f)


def post_install(self):
    for shell in ["bash", "fish", "zsh"]:
        self.install_completion(f"nerdctl.{shell}", shell)
