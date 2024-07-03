pkgname = "buildkit"
pkgver = "0.14.1"
pkgrel = 3
build_style = "go"
make_build_args = ["./cmd/..."]
hostmakedepends = ["go"]
depends = ["containerd"]
pkgdesc = "Concurrent, cache-efficient, and Dockerfile-agnostic builder toolkit"
maintainer = "psykose <alice@ayaya.dev>"
license = "Apache-2.0"
url = "https://github.com/moby/buildkit"
source = f"https://github.com/moby/buildkit/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "5a587973a76173a5e42af0a3d25999596b5374e4b2f373c51cd07e64aa779da0"
# debug: objcopy ppc64
# check: cannot work in bwrap
options = ["!debug", "!check"]


def post_install(self):
    self.install_tmpfiles(self.files_path / "tmpfiles.conf")
    self.install_service(self.files_path / "buildkitd")
