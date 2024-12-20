pkgname = "docker-compose"
pkgver = "2.32.1"
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
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "Apache-2.0"
url = "https://docs.docker.com/compose"
source = f"https://github.com/docker/compose/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "730a55f6746fdb0b0258ea45d2d9070e6e3a10db901342daa3056f4c4262c50e"
# need a running docker daemon
options = ["!check"]


def install(self):
    self.install_file(
        f"{self.make_dir}/cmd",
        "usr/libexec/docker/cli-plugins",
        name="docker-compose",
    )
