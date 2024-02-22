pkgname = "headscale"
pkgver = "0.22.3"
pkgrel = 0
build_style = "go"
make_build_args = [
    f"-ldflags=-X github.com/juanfont/headscale/cmd/headscale/cli.Version=v{pkgver}",
    "./cmd/headscale",
]
make_check_args = ["./..."]
hostmakedepends = ["go"]
pkgdesc = "Open source implementation of the tailscale control server"
maintainer = "psykose <alice@ayaya.dev>"
license = "BSD-3-Clause"
url = "https://github.com/juanfont/headscale"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "ee408065c879fc5148a10050d663f93148eccdd6bf59d3b953673a36eaad4070"
# generates completions with host binary
options = ["!cross"]


def post_install(self):
    self.install_license("LICENSE")
    self.install_service(self.files_path / "headscale")
    self.install_file("config-example.yaml", "usr/share/headscale")
    self.install_file(
        self.files_path / "sysusers.conf",
        "usr/lib/sysusers.d",
        name="headscale.conf",
    )
    self.install_file(
        self.files_path / "tmpfiles.conf",
        "usr/lib/tmpfiles.d",
        name="headscale.conf",
    )
    for shell in ["bash", "fish", "zsh"]:
        with open(self.cwd / f"headscale.{shell}", "w") as f:
            self.do(
                self.chroot_cwd / self.make_dir / "headscale",
                "completion",
                shell,
                stdout=f,
            )
        self.install_completion(f"headscale.{shell}", shell)
