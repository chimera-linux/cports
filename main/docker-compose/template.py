pkgname = "docker-compose"
pkgver = "5.1.3"
pkgrel = 2
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
sha256 = "19c7219c97390473bb96530153e64fce98d4b05ecf6f73016e564201d99512e7"
# need a running docker daemon
options = ["!check"]


def install(self):
    self.install_file(
        f"{self.make_dir}/cmd",
        "usr/lib/docker/cli-plugins",
        name="docker-compose",
    )
