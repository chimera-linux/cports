pkgname = "python-boto3"
pkgver = "1.34.117"
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
sha256 = "d983e6049c53ca86e3457f0c4f58dc1e1e939cd72ee5f2afa1718b9e4db25ce8"


def init_check(self):
    self.make_check_args += [f"--numprocesses={self.make_jobs}"]
