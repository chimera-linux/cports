pkgname = "tflint"
pkgver = "0.59.1"
pkgrel = 2
build_style = "go"
hostmakedepends = ["go"]
pkgdesc = "Terraform Linter"
license = "MPL-2.0"
url = "https://github.com/terraform-linters/tflint"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "9b45910e897fd2028d748387abc781f13c57127bacde97b083aed2198c7b105d"
# Tests requires network connection
options = ["!check"]
