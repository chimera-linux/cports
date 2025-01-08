pkgname = "docker-compose"
pkgver = "2.32.2"
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
sha256 = "5bad84c26e31c790a2f09968bac6f57ed2d23c3f12b723a132fa854d4f8f5537"
# need a running docker daemon
options = ["!check"]


def install(self):
    self.install_file(
        f"{self.make_dir}/cmd",
        "usr/libexec/docker/cli-plugins",
        name="docker-compose",
    )
