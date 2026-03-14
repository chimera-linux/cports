pkgname = "yt-dlp-ejs"
# the version must match the version specified in yt-dlp's pyproject.toml
# https://github.com/yt-dlp/yt-dlp/wiki/EJS#option-1-install-the-yt-dlp-ejs-python-package
pkgver = "0.5.0"
pkgrel = 0
build_style = "python_pep517"
prepare_after_patch = True
hostmakedepends = [
    "nodejs",
    "python-build",
    "python-hatch_vcs",
    "python-hatchling",
    "python-installer",
]
checkdepends = ["python-pytest"]
pkgdesc = "External JavaScript for yt-dlp"
license = "Unlicense"
url = "https://github.com/yt-dlp/ejs"
source = f"$(PYPI_SITE)/y/yt_dlp_ejs/yt_dlp_ejs-{pkgver}.tar.gz"
sha256 = "8dfae59e418232f485253dcf8e197fefa232423c3af7824fe19e4517b173293b"


def prepare(self):
    self.do("npm", "ci", allow_network=True)
    self.do(
        "node",
        "--experimental-strip-types",
        "src/yt/solver/test/download.ts",
        allow_network=True,
    )


def check(self):
    from cbuild.util import python

    # the test_modules.py assumes that core.min.js and lib.min.js will be
    # present in chroot_cwd so rather than patching the test_modules.py file,
    # move it to the default dest in pybin
    envpy = python.setup_wheel_venv(self, ".cbuild-checkenv")
    self.cp(
        "test/test_modules.py",
        f".cbuild-checkenv/lib/python{self.python_version}/site-packages/yt_dlp_ejs",
    )
    self.do(
        envpy,
        "-m",
        "pytest",
        wrksrc=f".cbuild-checkenv/lib/python{self.python_version}/site-packages/yt_dlp_ejs",
    )

    self.do("node", "--test")


@subpackage("yt-dlp-ejs-nodejs")
def _(self):
    self.subdesc = "nodejs runtime"
    self.install_if = [self.parent]
    self.depends = ["nodejs"]
    self.options = ["empty"]
    return []
