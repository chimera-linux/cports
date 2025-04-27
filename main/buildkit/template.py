pkgname = "buildkit"
pkgver = "0.23.0"
pkgrel = 0
build_style = "go"
make_build_args = ["./cmd/..."]
hostmakedepends = ["go"]
depends = ["containerd", "rootlesskit"]
pkgdesc = "Concurrent, cache-efficient, and Dockerfile-agnostic builder toolkit"
license = "Apache-2.0"
url = "https://github.com/moby/buildkit"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "2f1390fcff4de26287da1339ee8e99a72ccea02d092d1139b8172019218d9071"
# cannot work in bwrap
options = ["!check"]


def post_install(self):
    self.install_tmpfiles(self.files_path / "tmpfiles.conf")
    self.install_service(self.files_path / "buildkitd")
    self.install_service(self.files_path / "buildkitd.user")
