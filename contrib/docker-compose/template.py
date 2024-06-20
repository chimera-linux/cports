pkgname = "docker-compose"
pkgver = "2.27.2"
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
sha256 = "1769596433f68fa68ed67974e796ddb71a96064f18e0d79f5c4259ed5c1be98b"
# need a running docker daemon
options = ["!debug", "!check"]


def do_install(self):
    self.install_file(
        f"{self.make_dir}/cmd",
        "usr/libexec/docker/cli-plugins",
        name="docker-compose",
    )
