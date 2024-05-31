pkgname = "python-botocore"
pkgver = "1.34.116"
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
checkdepends = depends + ["python-pytest"]
pkgdesc = "Core module supporting boto3 and aws cli"
maintainer = "ttyyls <contact@behri.org>"
license = "Apache-2.0"
url = "https://github.com/boto/botocore"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "90eb6b13391833c6f8f76a990a4835f8c5b02ea20a205e75bb3f25bf56611cc9"
# takes forever
options = ["!check"]
