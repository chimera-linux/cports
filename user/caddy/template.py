pkgname = "caddy"
pkgver = "2.11.1"
pkgrel = 0
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
sha256 = "6d0a9e90b3a7ea0b385a66003f493c1a7317f47d57faadd0ee7d82798b7d89e3"
# generates completions with host binary
options = ["!cross"]


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
