pkgname = "headscale"
pkgver = "0.29.3"
pkgrel = 1
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
sha256 = "9c2b6020b51a1d53641fe8e282fd849b4d00eca8945fef93d63454655a90ba0d"
# generates completions with host binary
options = ["!cross"]

if self.profile().arch == "ppc64le":
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
