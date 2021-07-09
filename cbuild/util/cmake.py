from cbuild.core import paths

def configure(pkg, cmake_dir = None, build_dir = "build", extra_args = []):
    if cmake_dir:
        cdir = str(pkg.chroot_wrksrc / cmake_dir)
    else:
        cdir = str(pkg.chroot_wrksrc)

    (pkg.abs_build_wrksrc / build_dir).mkdir(parents = True, exist_ok = True)

    mdir = str(paths.masterdir())
    cargs = []

    if pkg.bootstrapping:
        with open(
            pkg.abs_build_wrksrc / build_dir / "bootstrap.cmake", "w"
        ) as infile:
            infile.write(f"""
SET(CMAKE_SYSTEM_NAME Linux)
SET(CMAKE_SYSTEM_VERSION 1)

SET(CMAKE_C_COMPILER   {pkg.tools["CC"]})
SET(CMAKE_CXX_COMPILER {pkg.tools["CXX"]})

SET(CMAKE_FIND_ROOT_PATH  "{mdir}/usr;{mdir}")

SET(CMAKE_FIND_ROOT_PATH_MODE_LIBRARY ONLY)
SET(CMAKE_FIND_ROOT_PATH_MODE_INCLUDE ONLY)
""")
        cargs.append("-DCMAKE_TOOLCHAIN_FILE=bootstrap.cmake")

    pkg.do(
        "cmake", cargs + [
            "-DCMAKE_INSTALL_PREFIX=/usr",
            "-DCMAKE_BUILD_TYPE=None",
            "-DCMAKE_INSTALL_LIBDIR=lib",
            "-DCMAKE_INSTALL_SBINDIR=bin"
        ] + pkg.configure_args + extra_args + [cdir],
        wrksrc = build_dir, build = True, env = {
            "CMAKE_GENERATOR": (
                "Ninja" if pkg.make_cmd == "ninja" else "Unix Makefiles"
            )
        }
    )
