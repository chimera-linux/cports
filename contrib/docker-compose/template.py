pkgname = "docker-compose"
pkgver = "2.24.6"
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
maintainer = "psykose <alice@ayaya.dev>"
license = "Apache-2.0"
url = "https://docs.docker.com/compose"
source = f"https://github.com/docker/compose/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "14fffeba19b82c8e5a9cdf6d873522a11ee4e25bbb86bbdf468795274429db70"
# need a running docker daemon
options = ["!debug", "!check"]


def do_install(self):
    self.install_file(
        f"{self.make_dir}/cmd",
        "usr/libexec/docker/cli-plugins",
        name="docker-compose",
    )
