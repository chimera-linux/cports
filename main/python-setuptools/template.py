pkgname = "python-setuptools"
version = "57.0.0"
revision = 0
wrksrc = f"setuptools-{version}"
build_style = "python_module"
hostmakedepends = ["python-devel"]
depends = ["python"]
short_desc = "Easily build and distribute Python packages"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
homepage = "https://github.com/pypa/setuptools"
distfiles = [f"$(PYPI_SITE)/s/setuptools/setuptools-{version}.tar.gz"]
checksum = ["401cbf33a7bf817d08014d51560fc003b895c4cdc1a5b521ad2969e928a07535"]

options = ["!check"]

env = {
    "SETUPTOOLS_INSTALL_WINDOWS_SPECIFIC_FILES": "0",
    "SETUPTOOLS_DISABLE_VERSIONED_EASY_INSTALL_SCRIPT": "1"
}

def post_install(self):
    self.install_license("LICENSE")
