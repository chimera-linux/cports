pkgname = "protontricks"
pkgver = "1.14.0"
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
sha256 = "378e79dee69a8a33409e350f6e476891f8e9ce7ac2709fe69495e1be4ba009e7"
