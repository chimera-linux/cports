pkgname = "dinit"
pkgver = "0.19.0"
# temporary so we get our features
_gitrev = "92cb58eedaf930fed60d17b6247c1f2155c78ec8"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--syscontrolsocket=/run/dinitctl"]
configure_gen = []
make_dir = "."
make_check_args = ["check-igr"]  # additional target
pkgdesc = "Service manager and init system"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Apache-2.0"
url = "https://davmac.org/projects/dinit"
source = f"https://github.com/davmac314/dinit/archive/{_gitrev}.tar.gz"
sha256 = "dba72f3ca0d8cbd50d5f36f49aad4c1eaad8b30a66fac3abd6f8785cafb00e73"
tool_flags = {"CXXFLAGS": ["-fno-rtti"]}
hardening = ["vis", "cfi"]
