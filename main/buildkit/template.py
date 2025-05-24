pkgname = "buildkit"
pkgver = "0.22.0"
pkgrel = 0
build_style = "go"
make_build_args = ["./cmd/..."]
hostmakedepends = ["go"]
depends = ["containerd", "rootlesskit"]
pkgdesc = "Concurrent, cache-efficient, and Dockerfile-agnostic builder toolkit"
license = "Apache-2.0"
url = "https://github.com/moby/buildkit"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "3c028d69dba6d74075326596892757c0f59bb7aad8f4eb4cacaddc2d6a6311b5"
# cannot work in bwrap
options = ["!check"]


def post_install(self):
    self.install_tmpfiles(self.files_path / "tmpfiles.conf")
    self.install_service(self.files_path / "buildkitd")
    self.install_service(self.files_path / "buildkitd.user")
