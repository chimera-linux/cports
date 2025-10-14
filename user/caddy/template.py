pkgname = "caddy"
pkgver = "2.10.2"
pkgrel = 1
build_style = "go"
make_build_args = [
    f"-ldflags=-X github.com/caddyserver/caddy/v2.CustomVersion=v{pkgver}",
    "./cmd/caddy",
]
make_check_args = ["-p", "1", "./..."]
hostmakedepends = ["go"]
makedepends = ["dinit-chimera"]
depends = ["shared-mime-info"]
pkgdesc = "Extensible HTTP server with automatic HTTPS"
license = "Apache-2.0"
url = "https://caddyserver.com"
source = f"https://github.com/caddyserver/caddy/archive/v{pkgver}.tar.gz"
sha256 = "f63f46b7ae68ced0a5c2e31df1b6dfc7656117d162a1bc7fed4bd4afd14ddc8f"
# generates completions with host binary
options = ["!check"]


def post_build(self):
    for shell in ["bash", "fish", "zsh"]:
        with open(self.cwd / f"caddy.{shell}", "w") as outf:
            self.do(
                "build/caddy",
                "completion",
                shell,
                stdout=outf,
            )


def post_install(self):
    self.install_sysusers(self.files_path / "sysusers.conf")
    self.install_tmpfiles(self.files_path / "tmpfiles.conf")
    self.install_service(self.files_path / "caddy")

    for shell in ["bash", "fish", "zsh"]:
        self.install_completion(f"caddy.{shell}", shell)
