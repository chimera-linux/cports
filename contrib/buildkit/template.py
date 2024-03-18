pkgname = "buildkit"
pkgver = "0.13.1"
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
sha256 = "96466d2a51d5327e9a1e5e99fe2a229ba2b3ff62175f0c45e4e9b82e904fdc65"
# debug: objcopy ppc64
# check: cannot work in bwrap
options = ["!debug", "!check"]


def post_extract(self):
    # delete stray incomplete vendor dir
    self.rm("vendor/", recursive=True)


def post_install(self):
    self.install_dir("var/lib/buildkit", empty=True)
    self.install_service(self.files_path / "buildkitd")
