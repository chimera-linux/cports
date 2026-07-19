pkgname = "docker-compose"
pkgver = "5.3.1"
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
sha256 = "1823e1b09c4082779fdf5cc9f3d8453b95dba3d939105b39366175ce12fdb6c7"
# need a running docker daemon
options = ["!check"]


def install(self):
    self.install_file(
        f"{self.make_dir}/cmd",
        "usr/lib/docker/cli-plugins",
        name="docker-compose",
    )
