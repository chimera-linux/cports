pkgname = "buildkit"
pkgver = "0.17.2"
pkgrel = 0
build_style = "go"
make_build_args = ["./cmd/..."]
hostmakedepends = ["go"]
depends = ["containerd"]
pkgdesc = "Concurrent, cache-efficient, and Dockerfile-agnostic builder toolkit"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "Apache-2.0"
url = "https://github.com/moby/buildkit"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "0dce3869150bb6625d05f35b491a66a206f0db4fdc8a688b0bf621b48a11d92a"
# cannot work in bwrap
options = ["!check"]


def post_install(self):
    self.install_tmpfiles(self.files_path / "tmpfiles.conf")
    self.install_service(self.files_path / "buildkitd")
