pkgname = "podman-compose"
pkgver = "1.2.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
]
depends = [
    "podman",
    "python-dotenv",
    "python-pyyaml",
]
checkdepends = ["python-pytest", *depends]
pkgdesc = "Podman utility for docker-compose.yml support"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "GPL-2.0-only"
url = "https://github.com/containers/podman-compose"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "211b235cf6ffe38f5f65fa188471e4b2706895c1ef4e800bb2a59a01f272674e"
# tests need to run podman which isn't gonna work in bwrap without networking and so on
options = ["!check"]


def post_install(self):
    self.install_completion("./completion/bash/podman-compose", "bash")
