pkgname = "terragrunt"
pkgver = "0.99.5"
pkgrel = 0
build_style = "go"
hostmakedepends = ["go"]
checkdepends = ["bash"]
pkgdesc = "Orchestration tool for writing OpenTofu at scale"
license = "MIT"
url = "https://github.com/gruntwork-io/terragrunt"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "372fce15517952639089c259f5fa453fed103a58aec41ca8abe671af75e51fbe"
# tests perform many 'git clone's
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE.txt")
