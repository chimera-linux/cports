pkgname = "docker-compose"
pkgver = "5.8.0"
pkgrel = 0
build_style = "go"
make_build_args = [
    "-ldflags",
    f"-X github.com/docker/compose/v2/internal.Version=v{pkgver}",
    "./cmd",
]
hostmakedepends = ["go"]
depends = ["docker-cli"]
pkgdesc = "Docker CLI plugin for compose files"
license = "Apache-2.0"
url = "https://docs.docker.com/compose"
source = f"https://github.com/docker/compose/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "1836019594ad054f8459cea7efc1d52eae7d05c64217c4efffe02d0d2930c44b"
# need a running docker daemon
options = ["!check"]


def install(self):
    self.install_file(
        f"{self.make_dir}/cmd",
        "usr/lib/docker/cli-plugins",
        name="docker-compose",
    )
