pkgname = "buildkit"
pkgver = "0.28.0"
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
sha256 = "2307112b30593fb8fc4d479ce4547862fa101fa2ecd50a852330a1117a988bbc"
# cannot work in bwrap
options = ["!check"]


def post_install(self):
    self.install_tmpfiles(self.files_path / "tmpfiles.conf")
    self.install_service(self.files_path / "buildkitd")
    self.install_service(self.files_path / "buildkitd.user")
