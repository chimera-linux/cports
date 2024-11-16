pkgname = "python-acme"
pkgver = "3.0.1"
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
maintainer = "Duncan Bellamy <dunk@denkimushi.com>"
license = "Apache-2.0"
url = "https://github.com/certbot/certbot/tree/master/acme"
source = (
    f"https://github.com/certbot/certbot/archive/refs/tags/v{pkgver}.tar.gz"
)
sha256 = "241bc1b7bfaf9b00955a86274bc78336a15c3706ce838b59e8819325dee698cc"


def init_check(self):
    self.make_check_args += [
        f"--numprocesses={self.make_jobs}",
        "--dist=worksteal",
    ]


def post_install(self):
    self.install_license("LICENSE.txt")
