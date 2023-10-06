pkgname = "nerdctl"
pkgver = "1.6.0"
pkgrel = 1
build_style = "go"
make_build_args = ["./cmd/nerdctl"]
hostmakedepends = ["go"]
depends = ["containerd"]
pkgdesc = "Containerd CLI"
maintainer = "psykose <alice@ayaya.dev>"
license = "Apache-2.0"
url = "https://github.com/containerd/nerdctl"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "a369b1c517d9c3d53d00b29633a6176a05811214a44dd25d339c32cc6a901579"
# objcopy fails to split on ppc
# can't run tests inside namespaces
options = ["!debug", "!check"]


def post_build(self):
    for shell in ["bash", "fish", "zsh"]:
        with open(self.cwd / f"nerdctl.{shell}", "w") as f:
            self.do(
                self.chroot_cwd / self.make_dir / "nerdctl",
                "completion",
                shell,
                stdout=f,
            )


def post_install(self):
    for shell in ["bash", "fish", "zsh"]:
        self.install_completion(f"nerdctl.{shell}", shell)
