pkgname = "podman-compose"
pkgver = "1.4.1"
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
license = "GPL-2.0-only"
url = "https://github.com/containers/podman-compose"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "582c6021b03565d4fe71ddb5d12c5fbcdbc630ca24d2b29b02d568a2da304853"
# tests need to run podman which isn't gonna work in bwrap without networking and so on
options = ["!check"]


def post_install(self):
    self.install_completion("./completion/bash/podman-compose", "bash")
