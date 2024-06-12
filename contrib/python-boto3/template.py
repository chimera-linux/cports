pkgname = "python-boto3"
pkgver = "1.34.124"
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
checkdepends = depends + ["python-pytest-xdist"]
pkgdesc = "Python AWS SDK"
maintainer = "ttyyls <contact@behri.org>"
license = "Apache-2.0"
url = "https://github.com/boto/boto3"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "bb409462ec9683c229bc88f5c1f3868e1198b4cbf1cfdf8a9581a7db49a6e8f0"


def init_check(self):
    self.make_check_args += [f"--numprocesses={self.make_jobs}"]
