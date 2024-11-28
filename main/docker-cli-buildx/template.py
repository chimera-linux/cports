pkgname = "docker-cli-buildx"
pkgver = "0.19.1"
pkgrel = 0
build_style = "go"
make_build_args = [
    f"-ldflags=-X github.com/docker/buildx/version.Version=v{pkgver}",
    "./cmd/buildx",
]
make_install_args = [*make_build_args]
hostmakedepends = ["go"]
checkdepends = ["git"]
depends = ["docker-cli"]
pkgdesc = "Docker CLI plugin for extended build capabilities with BuildKit"
maintainer = "ttyyls <contact@behri.org>"
license = "Apache-2.0"
url = "https://github.com/docker/buildx"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "7a14199d052d4933bb5379207f13d4b6562ab10f3fb9f5217790b482bd2b25f4"
# some tests rely on network
options = ["!check"]


def install(self):
    self.install_file(
        "build/buildx",
        "usr/libexec/docker/cli-plugins",
        name="docker-buildx",
    )
