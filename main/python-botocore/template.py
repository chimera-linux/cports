pkgname = "python-botocore"
pkgver = "1.36.2"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
depends = [
    "python-dateutil",
    "python-jmespath",
    "python-urllib3",
]
checkdepends = ["python-pytest", *depends]
pkgdesc = "Core module supporting boto3 and aws cli"
maintainer = "ttyyls <contact@behri.org>"
license = "Apache-2.0"
url = "https://github.com/boto/botocore"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "a1aebc52d2bd08766bf41de5ffd67ab28a3ab4851b94b024691dbb42a19771d2"
# takes forever
options = ["!check"]
