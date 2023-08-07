pkgname = "buildkit"
pkgver = "0.12.1"
pkgrel = 0
build_style = "go"
make_build_args = ["./cmd/..."]
hostmakedepends = ["go"]
depends = ["containerd"]
pkgdesc = "Concurrent, cache-efficient, and Dockerfile-agnostic builder toolkit"
maintainer = "psykose <alice@ayaya.dev>"
license = "Apache-2.0"
url = "https://github.com/moby/buildkit"
source = f"https://github.com/moby/buildkit/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "85900c97b3857f102065a1da9ed448875c719d1282d820bc4875a9d1a14aef02"
# objcopy ppc64
options = ["!debug"]


def post_install(self):
    self.install_dir("var/lib/buildkit", empty=True)
    self.install_service(self.files_path / "buildkitd")
