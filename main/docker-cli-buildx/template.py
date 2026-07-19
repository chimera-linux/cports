pkgname = "docker-cli-buildx"
pkgver = "0.35.0"
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
license = "Apache-2.0"
url = "https://github.com/docker/buildx"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "790e4eb0c98da49c60d2c94cebcd3f1658cd7aca3be82093fcb19b9c1d0ac06b"
# some tests rely on network
options = ["!check"]


def install(self):
    self.install_file(
        "build/buildx",
        "usr/lib/docker/cli-plugins",
        name="docker-buildx",
    )
