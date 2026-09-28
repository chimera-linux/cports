pkgname = "python-acme"
pkgver = "5.7.0"
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
sha256 = "8cd3301ea564046730404a255da44b0a5e28df268eee9b9d9915b1369c55b1b9"


def init_check(self):
    self.make_check_args += [
        f"--numprocesses={self.make_jobs}",
        "--dist=worksteal",
    ]


def post_install(self):
    self.install_license("LICENSE.txt")
