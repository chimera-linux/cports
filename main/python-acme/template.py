pkgname = "python-acme"
pkgver = "4.0.0"
pkgrel = 0
build_wrksrc = "acme"
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
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
license = "Apache-2.0"
url = "https://github.com/certbot/certbot/tree/master/acme"
source = (
    f"https://github.com/certbot/certbot/archive/refs/tags/v{pkgver}.tar.gz"
)
sha256 = "8c365355ca9b4860312cdb6d56eb2254fff26877a6677b293b5e3307554496d2"


def init_check(self):
    self.make_check_args += [
        f"--numprocesses={self.make_jobs}",
        "--dist=worksteal",
    ]


def post_install(self):
    self.install_license("LICENSE.txt")
