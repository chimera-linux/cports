pkgname = "podman-compose"
pkgver = "1.3.0"
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
sha256 = "d2d641d23bead9cead06bdd2edb9d6a592a138fc8bb7ecb53f87e21e99d45af7"
# tests need to run podman which isn't gonna work in bwrap without networking and so on
options = ["!check"]


def post_install(self):
    self.install_completion("./completion/bash/podman-compose", "bash")
