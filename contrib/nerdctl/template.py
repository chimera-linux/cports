pkgname = "nerdctl"
pkgver = "1.6.2"
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
sha256 = "fb7660f7e598e4c502d4f0c26cf985290fc7bdc80cce1f7402020afdf83ef988"
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
