pkgname = "python-boto3"
pkgver = "1.35.54"
pkgrel = 0
build_style = "python_pep517"
make_check_args = [
    # need credentials
    "--deselect=tests/integration",
    # takes forever
    "--deselect=tests/functional/docs/test_smoke.py::test_documentation[quicksight]",
    "--dist=worksteal",
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
checkdepends = ["python-pytest-xdist", *depends]
pkgdesc = "Python AWS SDK"
maintainer = "ttyyls <contact@behri.org>"
license = "Apache-2.0"
url = "https://github.com/boto/boto3"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "4e3884683fa3b01a01a3861e9c217db1f2c884b6d4caf6e9d9208de51be188f4"


def init_check(self):
    self.make_check_args += [f"--numprocesses={self.make_jobs}"]
