pkgname = "python-boto3"
pkgver = "1.35.75"
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
sha256 = "8d5ded13d7b4427679e98e31c48be6b395a2cec1b36e1903a5ba0af85d4a34dd"


def init_check(self):
    self.make_check_args += [f"--numprocesses={self.make_jobs}"]
