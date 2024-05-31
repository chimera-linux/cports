pkgname = "python-boto3"
pkgver = "1.34.116"
pkgrel = 0
build_style = "python_pep517"
make_check_args = [
    # need credentials
    "--deselect=tests/integration",
]
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
depends = [
    "python-botocore",
    "python-jmespath",
    "python-s3transfer",
]
checkdepends = depends + ["python-pytest-xdist"]
pkgdesc = "Python AWS SDK"
maintainer = "ttyyls <contact@behri.org>"
license = "Apache-2.0"
url = "https://github.com/boto/boto3"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "54b11d69931298ca8c15f4647667e8a6925ba6aa1a7c4297395f12d76ec04fa4"


def init_check(self):
    self.make_check_args += [f"--numprocesses={self.make_jobs}"]
