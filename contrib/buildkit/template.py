pkgname = "buildkit"
pkgver = "0.15.1"
pkgrel = 2
build_style = "go"
make_build_args = ["./cmd/..."]
hostmakedepends = ["go"]
depends = ["containerd"]
pkgdesc = "Concurrent, cache-efficient, and Dockerfile-agnostic builder toolkit"
maintainer = "psykose <alice@ayaya.dev>"
license = "Apache-2.0"
url = "https://github.com/moby/buildkit"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "5ee1ccf7d376c5e399c50ae400cfc24ec3c682df8139e8ba46f41ea261f10b4f"
# cannot work in bwrap
options = ["!check"]


def post_install(self):
    self.install_tmpfiles(self.files_path / "tmpfiles.conf")
    self.install_service(self.files_path / "buildkitd")
