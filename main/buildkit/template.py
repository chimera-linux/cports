pkgname = "buildkit"
pkgver = "0.25.1"
pkgrel = 0
build_style = "go"
make_build_args = ["./cmd/..."]
hostmakedepends = ["go"]
makedepends = ["dinit-chimera"]
depends = ["containerd", "rootlesskit"]
pkgdesc = "Concurrent, cache-efficient, and Dockerfile-agnostic builder toolkit"
license = "Apache-2.0"
url = "https://github.com/moby/buildkit"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "77a6586ccb11d5164aada9906701d226aaab567dbf7b5508bcb61b5bc45e6b46"
# cannot work in bwrap
options = ["!check"]


def post_install(self):
    self.install_tmpfiles(self.files_path / "tmpfiles.conf")
    self.install_service(self.files_path / "buildkitd")
    self.install_service(self.files_path / "buildkitd.user")
