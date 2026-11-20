pkgname = "docker-cli-buildx"
pkgver = "0.39.1"
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
sha256 = "ccb549da4ec19317a04e68c9a3603553503743b8deee0e0613e0cb06c87ed6bc"
# some tests rely on network
options = ["!check"]


def install(self):
    self.install_file(
        "build/buildx",
        "usr/lib/docker/cli-plugins",
        name="docker-buildx",
    )
