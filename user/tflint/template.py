pkgname = "tflint"
pkgver = "0.62.0"
pkgrel = 0
build_style = "go"
hostmakedepends = ["go"]
pkgdesc = "Terraform Linter"
license = "MPL-2.0"
url = "https://github.com/terraform-linters/tflint"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "e3736da82afb3a77037f72b9a01f2d5a60560664ed927426627ef7cfa3356fdd"
# Tests requires network connection
options = ["!check"]
