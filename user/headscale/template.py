pkgname = "headscale"
pkgver = "0.29.7"
pkgrel = 0
build_style = "go"
prepare_after_patch = True
make_build_args = [
    f"-ldflags=-X github.com/juanfont/headscale/cmd/headscale/cli.Version=v{pkgver}",
    "./cmd/headscale",
]
make_check_args = ["-short", "./..."]
hostmakedepends = ["go"]
makedepends = ["dinit-chimera"]
pkgdesc = "Open source implementation of the tailscale control server"
license = "BSD-3-Clause"
url = "https://github.com/juanfont/headscale"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "625e8f877ddcbacd0936dcd9bb191ea7b8914ef9f653b3e1a3b5fa6c611a36c8"
# generates completions with host binary
options = ["!cross"]

if self.profile.arch == "ppc64le":
    broken = "segfaults in tests"


def post_build(self):
    for shell in ["bash", "fish", "zsh"]:
        with open(self.cwd / f"headscale.{shell}", "w") as f:
            self.do(f"{self.make_dir}/headscale", "completion", shell, stdout=f)


def post_install(self):
    self.install_license("LICENSE")
    self.install_service(self.files_path / "headscale")
    self.install_file("config-example.yaml", "usr/share/headscale")
    self.install_sysusers(self.files_path / "sysusers.conf")
    self.install_tmpfiles(self.files_path / "tmpfiles.conf")
    for shell in ["bash", "fish", "zsh"]:
        self.install_completion(f"headscale.{shell}", shell)
