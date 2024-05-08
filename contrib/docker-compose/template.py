pkgname = "docker-compose"
pkgver = "2.27.0"
pkgrel = 1
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
sha256 = "29b2232d1609dff03db74188a7944c85ba8b612f47a7e39938a43db8fb7d7067"
# need a running docker daemon
options = ["!debug", "!check"]


def do_install(self):
    self.install_file(
        f"{self.make_dir}/cmd",
        "usr/libexec/docker/cli-plugins",
        name="docker-compose",
    )
