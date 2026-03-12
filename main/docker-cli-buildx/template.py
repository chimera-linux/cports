pkgname = "docker-cli-buildx"
pkgver = "0.32.1"
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
sha256 = "fc4b82f21f766a704fb26239550d37dfed3936b6e76580cddb00407f13f48f6d"
# some tests rely on network
options = ["!check"]


def install(self):
    self.install_file(
        "build/buildx",
        "usr/libexec/docker/cli-plugins",
        name="docker-buildx",
    )
