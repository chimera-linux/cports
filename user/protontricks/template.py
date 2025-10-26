pkgname = "protontricks"
pkgver = "1.13.0"
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
license = "GPL-3.0-only"
url = "https://github.com/Matoking/protontricks"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "bacf9890d5578f5e0cd7b3da764669de02a750a27db23a7154e45dcd3c6f7790"
