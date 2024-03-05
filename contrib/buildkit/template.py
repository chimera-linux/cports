pkgname = "buildkit"
pkgver = "0.13.0"
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
sha256 = "6b7cece44acce189870d7fe68521d1f9b2fbc07e791843f77f930b6ad82057b4"
# objcopy ppc64
options = ["!debug"]


def post_extract(self):
    # delete stray incomplete vendor dir
    self.rm("vendor/", recursive=True)


def post_install(self):
    self.install_dir("var/lib/buildkit", empty=True)
    self.install_service(self.files_path / "buildkitd")
