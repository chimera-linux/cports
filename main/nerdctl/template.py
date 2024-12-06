pkgname = "nerdctl"
pkgver = "2.0.1"
pkgrel = 0
build_style = "go"
make_build_args = ["./cmd/nerdctl"]
hostmakedepends = ["go"]
depends = ["containerd", "iptables"]
pkgdesc = "Containerd CLI"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "Apache-2.0"
url = "https://github.com/containerd/nerdctl"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "916d67ca74f343f6a169caed3187a71c338c342deaf253101ffd4e04e7a43d8b"
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
        "usr/bin/containerd-rootless",
        "usr/lib/dinit.d/user",
    ]
