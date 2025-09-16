pkgname = "buildkit"
pkgver = "0.23.2"
pkgrel = 1
build_style = "go"
make_build_args = ["./cmd/..."]
hostmakedepends = ["go"]
makedepends = ["dinit-chimera"]
depends = ["containerd", "rootlesskit"]
pkgdesc = "Concurrent, cache-efficient, and Dockerfile-agnostic builder toolkit"
license = "Apache-2.0"
url = "https://github.com/moby/buildkit"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "5f8e18b63bbf8e41dc787e8ce68103c94acb1585782cb42697aa1dfa252817d7"
# cannot work in bwrap
options = ["!check"]


def post_install(self):
    self.install_tmpfiles(self.files_path / "tmpfiles.conf")
    self.install_service(self.files_path / "buildkitd")
    self.install_service(self.files_path / "buildkitd.user")
