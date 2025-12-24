pkgname = "tflint"
pkgver = "0.60.0"
pkgrel = 0
build_style = "go"
hostmakedepends = ["go"]
pkgdesc = "Terraform Linter"
license = "MPL-2.0"
url = "https://github.com/terraform-linters/tflint"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "4a0c84fc4052de551f97e5c4b0b81f869e3ec708e4f27eff5157813c8b46fea3"
# Tests requires network connection
options = ["!check"]
