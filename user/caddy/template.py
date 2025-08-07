pkgname = "caddy"
pkgver = "2.10.0"
pkgrel = 3
build_style = "go"
make_build_args = [
    f"-ldflags=-X github.com/caddyserver/caddy/v2.CustomVersion=v{pkgver}",
    "./cmd/caddy",
]
make_check_args = ["-p", "1", "./..."]
hostmakedepends = ["go"]
depends = ["shared-mime-info"]
pkgdesc = "Extensible HTTP server with automatic HTTPS"
license = "Apache-2.0"
url = "https://caddyserver.com"
source = f"https://github.com/caddyserver/caddy/archive/v{pkgver}.tar.gz"
sha256 = "e07e2747c394a6549751950ec8f7457ed346496f131ee38538ae39cf89ebcc68"


def post_install(self):
    self.install_sysusers(self.files_path / "sysusers.conf")
    self.install_tmpfiles(self.files_path / "tmpfiles.conf")
    self.install_service(self.files_path / "caddy")
