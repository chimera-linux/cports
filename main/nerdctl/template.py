pkgname = "nerdctl"
pkgver = "2.1.1"
pkgrel = 0
build_style = "go"
make_build_args = ["./cmd/nerdctl"]
hostmakedepends = ["go"]
depends = ["containerd", "iptables"]
pkgdesc = "Containerd CLI"
license = "Apache-2.0"
url = "https://github.com/containerd/nerdctl"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "fb8dbdc8954aaf9dbf05396f51289a094a4927e385cc974bc410ecc3fcf16d03"
# can't run tests inside namespaces
# cross: generates completions with host binary
options = ["!check", "!cross"]


def post_build(self):
    for shell in ["bash", "fish", "zsh"]:
        with open(self.cwd / f"nerdctl.{shell}", "w") as f:
            self.do(f"{self.make_dir}/nerdctl", "completion", shell, stdout=f)


def post_install(self):
    for shell in ["bash", "fish", "zsh"]:
        self.install_completion(f"nerdctl.{shell}", shell)
