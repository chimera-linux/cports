pkgname = "nerdctl"
pkgver = "1.7.7"
pkgrel = 2
build_style = "go"
make_build_args = ["./cmd/nerdctl"]
hostmakedepends = ["go"]
depends = ["containerd", "iptables"]
pkgdesc = "Containerd CLI"
maintainer = "psykose <alice@ayaya.dev>"
license = "Apache-2.0"
url = "https://github.com/containerd/nerdctl"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "bcddf2ee3ad2bc84adc5e207f97157998fe973912c7d1dd9540bd4bb4a07698d"
# can't run tests inside namespaces
# cross: generates completions with host binary
options = ["!check", "!cross"]


def post_build(self):
    for shell in ["bash", "fish", "zsh"]:
        with open(self.cwd / f"nerdctl.{shell}", "w") as f:
            self.do(f"{self.make_dir}/nerdctl", "completion", shell, stdout=f)


def post_install(self):
    self.install_service(self.files_path / "containerd.user")
    self.install_bin(
        "extras/rootless/containerd-rootless.sh", name="containerd-rootless"
    )
    for shell in ["bash", "fish", "zsh"]:
        self.install_completion(f"nerdctl.{shell}", shell)


@subpackage("containerd-rootless")
def _(self):
    self.pkgdesc = "Rootless containerd support"
    self.depends = [
        "containerd",
        "rootlesskit",
        "slirp4netns",
    ]

    return [
        "etc/dinit.d/user",
        "usr/bin/containerd-rootless",
    ]
