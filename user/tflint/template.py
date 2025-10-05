pkgname = "tflint"
pkgver = "0.58.0"
pkgrel = 3
build_style = "go"
hostmakedepends = ["go"]
pkgdesc = "Terraform Linter"
license = "MPL-2.0"
url = "https://github.com/terraform-linters/tflint"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "c65176cfc5d9c7291b1f240e469670bf222baf8fdf2b9b3555bf0b6fce74a4c7"
# Tests requires network connection
options = ["!check"]
