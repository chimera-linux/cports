pkgname = "python-distro"
pkgver = "1.9.0"
pkgrel = 1
build_style = "python_pep517"
make_check_args = [
    "--deselect=tests/test_distro.py::TestLSBRelease::test_linuxmint17_lsb_release",
    "--deselect=tests/test_distro.py::TestLSBRelease::test_manjaro1512_lsb_release",
    "--deselect=tests/test_distro.py::TestLSBRelease::test_ubuntu14normal_lsb_release",
    "--deselect=tests/test_distro.py::TestLSBRelease::test_ubuntu14nomodules_lsb_release",
    "--deselect=tests/test_distro.py::TestLSBRelease::test_trailingblanks_lsb_release",
    "--deselect=tests/test_distro.py::TestOverall::test_mageia5_release",
    "--deselect=tests/test_distro.py::TestOverall::test_manjaro1512_release",
    "--deselect=tests/test_distro.py::TestOverall::test_sles12_release",
    "--deselect=tests/test_distro.py::TestOverall::test_mandriva2011_release",
    "--deselect=tests/test_distro.py::TestOverallWithEtcNotReadable::test_mageia5_release",
    "--deselect=tests/test_distro.py::TestOverallWithEtcNotReadable::test_manjaro1512_release",
    "--deselect=tests/test_distro.py::TestOverallWithEtcNotReadable::test_sles12_release",
    "--deselect=tests/test_distro.py::TestOverallWithEtcNotReadable::test_mandriva2011_release",
]
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
depends = ["python"]
checkdepends = ["python-pytest"]
pkgdesc = "Linux OS platform information API"
maintainer = "Duncan Bellamy <dunk@denkimushi.com>"
license = "Apache-2.0"
url = "https://github.com/python-distro/distro"
source = f"$(PYPI_SITE)/d/distro/distro-{pkgver}.tar.gz"
sha256 = "2fa77c6fd8940f116ee1d6b94a2f90b13b5ea8d019b98bc8bafdcabcdd9bdbed"
