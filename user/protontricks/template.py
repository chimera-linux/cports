pkgname = "protontricks"
pkgver = "1.12.0"
pkgrel = 0
build_style = "python_pep517"
make_build_env = {"SETUPTOOLS_SCM_PRETEND_VERSION": pkgver}
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools_scm",
]
depends = [
    "python-pillow",
    "python-setuptools",
    "python-vdf",
    "winetricks",
    "zenity",
]
checkdepends = [
    "bash",
    "python-pytest",
    *depends,
]
pkgdesc = "Winetricks wrapper for Steam games"
maintainer = "Erica Z <zerica@callcc.eu>"
license = "GPL-3.0-only"
url = "https://github.com/Matoking/protontricks"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "6714e8fdd6f279659490a0fb85fc05b42bc91eb877a2b5febeb384f60ffb1051"
