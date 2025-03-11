pkgname = "buildkit"
pkgver = "0.20.1"
pkgrel = 0
build_style = "go"
make_build_args = ["./cmd/..."]
hostmakedepends = ["go"]
depends = ["containerd"]
pkgdesc = "Concurrent, cache-efficient, and Dockerfile-agnostic builder toolkit"
license = "Apache-2.0"
url = "https://github.com/moby/buildkit"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "f188a443233a1c3f9c2a66fdebc0d7667442e17da34a4f05d227bbf73168e820"
# cannot work in bwrap
options = ["!check"]


def post_install(self):
    self.install_tmpfiles(self.files_path / "tmpfiles.conf")
    self.install_service(self.files_path / "buildkitd")
