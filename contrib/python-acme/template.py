pkgname = "python-acme"
pkgver = "2.11.0"
pkgrel = 0
build_wrksrc = "acme"
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
depends = [
    "python-cryptography",
    "python-josepy",
    "python-openssl",
    "python-pyrfc3339",
    "python-pytz",
    "python-requests",
]
checkdepends = ["python-pytest-xdist", *depends]
pkgdesc = "ACME protocol implementation"
maintainer = "Duncan Bellamy <dunk@denkimushi.com>"
license = "Apache-2.0"
url = "https://github.com/certbot/certbot/tree/master/acme"
source = (
    f"https://github.com/certbot/certbot/archive/refs/tags/v{pkgver}.tar.gz"
)
sha256 = "93764a18e0b19fe5fc7471a02a2df1937c40eb65c86b3f9ea11b40416c1541dc"


def init_check(self):
    self.make_check_args += [
        f"--numprocesses={self.make_jobs}",
        "--dist=worksteal",
    ]


def post_install(self):
    self.install_license("LICENSE.txt")
