pkgname = "nerdctl"
pkgver = "1.5.0"
pkgrel = 0
build_style = "go"
make_build_args = ["./cmd/nerdctl"]
hostmakedepends = ["go"]
depends = ["containerd"]
pkgdesc = "Containerd CLI"
maintainer = "psykose <alice@ayaya.dev>"
license = "Apache-2.0"
url = "https://github.com/containerd/nerdctl"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "3b9ae94124adb5105241c3d5070b8dc0c184e454a7a349f1b56c12d415ee7ce3"
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
